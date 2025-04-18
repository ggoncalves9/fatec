from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
from models import db, bcrypt, Usuario, Questao, RespostaUsuario, Conquista, ConquistaUsuario, PontuacaoMensal
from ollama import AsyncClient
import asyncio
from question_agent import QuestionAgent

# Carrega variáveis de ambiente
load_dotenv()

app = Flask(__name__)

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.environ.get('DB_USER')}:{os.environ.get('DB_PASS')}@{os.environ.get('DB_HOST')}:{os.environ.get('DB_PORT')}/{os.environ.get('DB_NAME')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'sua_chave_secreta_aqui')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)

# Inicializa extensões
db.init_app(app)
bcrypt.init_app(app)
jwt_manager = JWTManager(app)

# Inicializa cliente Ollama
ollama_client = AsyncClient(host='http://ollama:11434')

# Inicializa agente de perguntas
question_agent = QuestionAgent(ollama_client)

# Rotas de autenticação
@app.route('/api/auth/registro', methods=['POST'])
def registro():
    data = request.get_json()
    
    # Verifica se o email já existe
    if Usuario.query.filter_by(email=data['email']).first():
        return jsonify({'erro': 'Email já cadastrado'}), 400
    
    # Cria novo usuário
    novo_usuario = Usuario(
        nome=data['nome'],
        email=data['email'],
        senha=data['senha']
    )
    
    db.session.add(novo_usuario)
    db.session.commit()
    
    return jsonify({'mensagem': 'Usuário criado com sucesso'}), 201

@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    usuario = Usuario.query.filter_by(email=data['email']).first()
    
    if usuario and usuario.verificar_senha(data['senha']):
        # Atualiza último login
        usuario.ultimo_login = datetime.utcnow()
        db.session.commit()
        
        # Cria token JWT
        access_token = create_access_token(identity=usuario.id)
        return jsonify({
            'access_token': access_token,
            'usuario': {
                'id': usuario.id,
                'nome': usuario.nome,
                'email': usuario.email
            }
        }), 200
    
    return jsonify({'erro': 'Email ou senha inválidos'}), 401

# Rotas do Ollama
@app.route('/api/ollama/models', methods=['GET'])
@jwt_required()
async def listar_modelos():
    modelos = await ollama_client.list_models()
    return jsonify({'modelos': modelos})

@app.route('/api/ollama/pull', methods=['POST'])
@jwt_required()
async def baixar_modelo():
    data = request.get_json()
    modelo = data.get('modelo')
    
    if not modelo:
        return jsonify({'erro': 'Nome do modelo não fornecido'}), 400
    
    sucesso = await ollama_client.pull_model(modelo)
    if sucesso:
        return jsonify({'mensagem': f'Modelo {modelo} baixado com sucesso'})
    return jsonify({'erro': f'Falha ao baixar modelo {modelo}'}), 500

@app.route('/api/ollama/chat', methods=['POST'])
@jwt_required()
async def chat_ollama():
    data = request.get_json()
    modelo = data.get('modelo', 'llama2')
    mensagens = data.get('mensagens', [])
    
    if not mensagens:
        return jsonify({'erro': 'Nenhuma mensagem fornecida'}), 400
    
    resposta = await ollama_client.chat(modelo, mensagens)
    return jsonify({'resposta': resposta})

# Rotas protegidas
@app.route('/api/perguntas/diarias', methods=['GET'])
@jwt_required()
def obter_perguntas_diarias():
    usuario_id = get_jwt_identity()
    
    # Obtém 5 perguntas aleatórias, balanceadas por dificuldade
    perguntas = Questao.query.order_by(db.func.random()).limit(5).all()
    
    return jsonify([{
        'id': q.id,
        'pergunta': q.pergunta,
        'opcoes': {
            'A': q.opcao_a,
            'B': q.opcao_b,
            'C': q.opcao_c,
            'D': q.opcao_d
        },
        'dificuldade': q.dificuldade,
        'tema': q.tema_estudo
    } for q in perguntas])

@app.route('/api/respostas', methods=['POST'])
@jwt_required()
def enviar_resposta():
    usuario_id = get_jwt_identity()
    data = request.get_json()
    
    questao = Questao.query.get(data['questao_id'])
    if not questao:
        return jsonify({'erro': 'Questão não encontrada'}), 404
    
    # Verifica resposta e calcula pontuação
    acertou = data['resposta'] == questao.resposta_correta
    pontuacao = questao.valor_score if acertou else 0
    
    # Salva resposta
    resposta = RespostaUsuario(
        usuario_id=usuario_id,
        questao_id=questao.id,
        resposta=data['resposta'],
        pontuacao=pontuacao
    )
    
    db.session.add(resposta)
    
    # Atualiza pontuação mensal
    hoje = datetime.utcnow()
    pontuacao_mensal = PontuacaoMensal.query.filter_by(
        usuario_id=usuario_id,
        mes=hoje.month,
        ano=hoje.year
    ).first()
    
    if not pontuacao_mensal:
        pontuacao_mensal = PontuacaoMensal(
            usuario_id=usuario_id,
            mes=hoje.month,
            ano=hoje.year
        )
        db.session.add(pontuacao_mensal)
    
    pontuacao_mensal.pontuacao_total += pontuacao
    db.session.commit()
    
    return jsonify({
        'acertou': acertou,
        'pontuacao': pontuacao,
        'explicacao': questao.explicacao
    })

@app.route('/api/pontuacao', methods=['GET'])
@jwt_required()
def obter_pontuacao():
    usuario_id = get_jwt_identity()
    hoje = datetime.utcnow()
    
    pontuacao_mensal = PontuacaoMensal.query.filter_by(
        usuario_id=usuario_id,
        mes=hoje.month,
        ano=hoje.year
    ).first()
    
    return jsonify({
        'pontuacao_total': pontuacao_mensal.pontuacao_total if pontuacao_mensal else 0,
        'posicao_ranking': pontuacao_mensal.posicao_ranking if pontuacao_mensal else None
    })

@app.route('/api/ranking', methods=['GET'])
@jwt_required()
def obter_ranking():
    hoje = datetime.utcnow()
    
    # Obtém ranking do mês atual
    ranking = PontuacaoMensal.query.filter_by(
        mes=hoje.month,
        ano=hoje.year
    ).order_by(PontuacaoMensal.pontuacao_total.desc()).limit(10).all()
    
    return jsonify([{
        'posicao': idx + 1,
        'usuario': {
            'id': r.usuario.id,
            'nome': r.usuario.nome
        },
        'pontuacao': r.pontuacao_total
    } for idx, r in enumerate(ranking)])

@app.route('/api/resposta', methods=['POST'])
@jwt_required()
def process_response():
    data = request.get_json()
    
    if not data or 'resposta' not in data:
        return jsonify({'error': 'Resposta não fornecida'}), 400
        
    response = data['resposta']
    current_user_id = get_jwt_identity()
    
    try:
        # Processa a resposta e obtém o feedback
        feedback = question_agent.process_response(response)
        
        # Obtém a próxima pergunta
        next_question = question_agent.get_current_question()
        
        return jsonify({
            'feedback': feedback,
            'next_question': next_question
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/perguntas', methods=['GET'])
def obter_perguntas():
    try:
        app.logger.info('Iniciando busca de perguntas...')
        
        # Obtém 5 perguntas aleatórias
        perguntas = Questao.query.order_by(db.func.random()).limit(5).all()
        
        app.logger.info(f'Encontradas {len(perguntas)} perguntas')
        
        if not perguntas:
            app.logger.warning('Nenhuma pergunta encontrada no banco de dados')
            return jsonify({'erro': 'Nenhuma pergunta encontrada'}), 404
            
        resultado = [pergunta.to_dict() for pergunta in perguntas]
        app.logger.info('Perguntas convertidas para JSON com sucesso')
        
        return jsonify(resultado)
    except Exception as e:
        app.logger.error(f'Erro ao obter perguntas: {str(e)}')
        return jsonify({'erro': f'Erro interno do servidor: {str(e)}'}), 500

@app.route('/api/iniciar-sessao', methods=['POST'])
@jwt_required()
def iniciar_sessao():
    """Inicia uma nova sessão de estudo"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'erro': 'Dados não fornecidos'}), 400

        aluno_id = get_jwt_identity()  # Pega o ID do usuário do token
        nivel = data.get('nivel', 'iniciante')  # Valor padrão: iniciante
        tema = data.get('tema', 'geral')  # Valor padrão: geral
        
        try:
            sessao_id = question_agent.create_session(aluno_id, nivel, tema)
            base_questions = question_agent.get_base_questions(tema, nivel)
            
            if not base_questions:
                return jsonify({'erro': 'Não há questões disponíveis para este tema/nível'}), 404
                
            primeira_questao = question_agent.generate_question(base_questions[0], nivel)
            
            return jsonify({
                'sessao_id': sessao_id,
                'pergunta': primeira_questao
            })
        except Exception as e:
            app.logger.error(f'Erro ao iniciar sessão: {str(e)}')
            return jsonify({'erro': 'Erro ao processar a sessão'}), 500
            
    except Exception as e:
        app.logger.error(f'Erro ao processar requisição: {str(e)}')
        return jsonify({'erro': 'Erro interno do servidor'}), 500

@app.route('/api/responder', methods=['POST'])
def responder():
    """Processa a resposta do aluno e retorna a próxima pergunta"""
    data = request.get_json()
    sessao_id = data.get('sessao_id')
    resposta = data.get('resposta')
    questao_atual = data.get('questao_atual')
    
    if not all([sessao_id, resposta, questao_atual]):
        return jsonify({'erro': 'Dados incompletos'}), 400
        
    try:
        # Avalia a resposta
        avaliacao = question_agent.evaluate_response(resposta, questao_atual)
        
        # Salva a resposta
        question_agent.save_response(
            sessao_id=sessao_id,
            questao_id=questao_atual['id'],
            pergunta=questao_atual['pergunta'],
            resposta=resposta,
            pontuacao=avaliacao['pontuacao'],
            feedback=avaliacao['feedback']
        )
        
        # Atualiza a pontuação da sessão
        question_agent.update_session_score(sessao_id, avaliacao['pontuacao'])
        
        # Verifica se a sessão está completa
        if question_agent.check_session_completion(sessao_id):
            question_agent.finish_session(sessao_id)
            resumo = question_agent.get_session_summary(sessao_id)
            return jsonify({
                'tipo': 'fim_sessao',
                'resumo': resumo,
                'feedback': avaliacao
            })
            
        # Gera próxima pergunta
        proxima_questao = question_agent.generate_question(
            question_agent.get_base_questions(
                questao_atual['tema'],
                questao_atual['nivel']
            )[0],
            questao_atual['nivel']
        )
        
        return jsonify({
            'tipo': 'proxima_pergunta',
            'feedback': avaliacao,
            'proxima_pergunta': proxima_questao
        })
        
    except Exception as e:
        app.logger.error(f'Erro ao processar resposta: {str(e)}')
        return jsonify({'erro': 'Erro interno do servidor'}), 500

@app.route('/api/ranking-semanal', methods=['GET'])
def ranking_semanal():
    """Obtém o ranking semanal"""
    try:
        cursor = db.session.execute("""
            SELECT 
                a.nome,
                r.pontuacao_total,
                r.media_pontuacao,
                r.posicao,
                r.nivel_mais_jogado
            FROM ranking_semanal r
            JOIN cad_aluno a ON r.aluno_id = a.id
            WHERE r.semana = EXTRACT(WEEK FROM CURRENT_DATE)
                AND r.ano = EXTRACT(YEAR FROM CURRENT_DATE)
            ORDER BY r.pontuacao_total DESC
            LIMIT 10
        """)
        
        ranking = [{
            'nome': row[0],
            'pontuacao': row[1],
            'media': float(row[2]),
            'posicao': row[3],
            'nivel': row[4]
        } for row in cursor]
        
        return jsonify(ranking)
    except Exception as e:
        app.logger.error(f'Erro ao obter ranking: {str(e)}')
        return jsonify({'erro': 'Erro interno do servidor'}), 500

@app.route('/health')
def health_check():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    with app.app_context():
        try:
            db.create_all()
            app.logger.info('Banco de dados inicializado com sucesso')
        except Exception as e:
            app.logger.error(f'Erro ao inicializar banco de dados: {str(e)}')
    app.run(host='0.0.0.0', port=5000)
