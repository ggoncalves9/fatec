from crewai import Agent, Task, Crew, Process
from langchain.tools import Tool
from langchain.agents import Tool
from langchain.llms import Ollama
import psycopg2
from datetime import datetime, date
import os

class QuestionAgent:
    def __init__(self):
        self.ollama = Ollama(base_url=f"http://{os.environ.get('OLLAMA_HOST')}:{os.environ.get('OLLAMA_PORT')}", model="llama2")
        self.db_conn = psycopg2.connect(
            host=os.environ.get('DB_HOST'),
            database=os.environ.get('DB_NAME'),
            user=os.environ.get('DB_USER'),
            password=os.environ.get('DB_PASS')
        )
        
    def get_base_questions(self, tema, dificuldade):
        """Obtém questões base do banco de dados para referência"""
        cursor = self.db_conn.cursor()
        cursor.execute("""
            SELECT pergunta, opcao_a, opcao_b, opcao_c, opcao_d, resposta_correta, explicacao
            FROM cad_questoes
            WHERE tema_estudo = %s AND dificuldade = %s
            ORDER BY RANDOM()
            LIMIT 5
        """, (tema, dificuldade))
        return cursor.fetchall()
        
    def create_session(self, aluno_id, nivel, tema):
        """Cria uma nova sessão de estudo"""
        cursor = self.db_conn.cursor()
        cursor.execute("""
            INSERT INTO sessoes_estudo (aluno_id, data_sessao, nivel_escolhido, tema_escolhido)
            VALUES (%s, %s, %s, %s)
            RETURNING id
        """, (aluno_id, date.today(), nivel, tema))
        self.db_conn.commit()
        return cursor.fetchone()[0]
        
    def save_response(self, sessao_id, questao_id, pergunta, resposta, pontuacao, feedback):
        """Salva a resposta do aluno"""
        cursor = self.db_conn.cursor()
        cursor.execute("""
            INSERT INTO historico_respostas 
            (sessao_id, questao_base_id, pergunta_gerada, resposta_aluno, pontuacao, feedback_ia)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (sessao_id, questao_id, pergunta, resposta, pontuacao, feedback))
        self.db_conn.commit()
        
    def update_session_score(self, sessao_id, pontos):
        """Atualiza a pontuação da sessão"""
        cursor = self.db_conn.cursor()
        cursor.execute("""
            UPDATE sessoes_estudo 
            SET pontuacao_sessao = pontuacao_sessao + %s,
                perguntas_respondidas = perguntas_respondidas + 1
            WHERE id = %s
        """, (pontos, sessao_id))
        self.db_conn.commit()

    def generate_question(self, base_question, nivel):
        """Gera uma pergunta usando o Ollama baseada na questão de referência"""
        prompt = f"""
        Com base na seguinte questão de referência de nível {nivel}:
        {base_question[0]}
        
        Opções:
        A) {base_question[1]}
        B) {base_question[2]}
        C) {base_question[3]}
        D) {base_question[4]}
        
        Gere uma nova pergunta sobre o mesmo tema, mantendo o nível de dificuldade,
        mas com uma abordagem diferente e criativa. Mantenha o formato de múltipla escolha.
        """
        
        response = self.ollama.predict(prompt)
        return response

    def evaluate_response(self, resposta_aluno, questao_base):
        """Avalia a resposta do aluno usando o Ollama"""
        prompt = f"""
        Avalie a seguinte resposta do aluno:
        
        Questão: {questao_base[0]}
        Resposta correta: {questao_base[5]}
        Explicação: {questao_base[6]}
        
        Resposta do aluno: {resposta_aluno}
        
        Forneça:
        1. Uma pontuação de 0 a 10
        2. Um feedback construtivo explicando os acertos e erros
        3. Dicas para melhorar o entendimento do tema
        """
        
        response = self.ollama.predict(prompt)
        return response

    def check_session_completion(self, sessao_id):
        """Verifica se a sessão está completa (5 perguntas)"""
        cursor = self.db_conn.cursor()
        cursor.execute("""
            SELECT perguntas_respondidas >= 5 as completa
            FROM sessoes_estudo
            WHERE id = %s
        """, (sessao_id,))
        return cursor.fetchone()[0]

    def finish_session(self, sessao_id):
        """Finaliza a sessão de estudo"""
        cursor = self.db_conn.cursor()
        cursor.execute("""
            UPDATE sessoes_estudo
            SET concluida = true,
                data_fim = CURRENT_TIMESTAMP
            WHERE id = %s
        """, (sessao_id,))
        self.db_conn.commit()

    def get_session_summary(self, sessao_id):
        """Obtém um resumo da sessão"""
        cursor = self.db_conn.cursor()
        cursor.execute("""
            SELECT pontuacao_sessao, nivel_escolhido, tema_escolhido,
                   date_part('minute', data_fim - data_inicio) as duracao_minutos
            FROM sessoes_estudo
            WHERE id = %s
        """, (sessao_id,))
        return cursor.fetchone()

    def update_weekly_ranking(self, aluno_id):
        """Atualiza o ranking semanal do aluno"""
        cursor = self.db_conn.cursor()
        cursor.execute("""
            INSERT INTO ranking_semanal (aluno_id, semana, ano, pontuacao_total, media_pontuacao)
            SELECT 
                aluno_id,
                EXTRACT(WEEK FROM data_sessao) as semana,
                EXTRACT(YEAR FROM data_sessao) as ano,
                SUM(pontuacao_sessao) as pontuacao_total,
                AVG(pontuacao_sessao) as media_pontuacao
            FROM sessoes_estudo
            WHERE aluno_id = %s
                AND data_sessao >= date_trunc('week', CURRENT_DATE)
            GROUP BY aluno_id, semana, ano
            ON CONFLICT (aluno_id, semana, ano) 
            DO UPDATE SET 
                pontuacao_total = EXCLUDED.pontuacao_total,
                media_pontuacao = EXCLUDED.media_pontuacao,
                data_atualizacao = CURRENT_TIMESTAMP
        """, (aluno_id,))
        self.db_conn.commit() 