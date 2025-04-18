from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
import uuid

db = SQLAlchemy()
bcrypt = Bcrypt()

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key=True)
    id_random = db.Column(UUID(as_uuid=True), default=uuid.uuid4)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha_hash = db.Column(db.String(255), nullable=False)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
    ultimo_login = db.Column(db.DateTime)
    
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha_hash = bcrypt.generate_password_hash(senha).decode('utf-8')
    
    def verificar_senha(self, senha):
        return bcrypt.check_password_hash(self.senha_hash, senha)

class Questao(db.Model):
    __tablename__ = 'cad_questoes'
    
    id = db.Column('id_quest', db.Integer, primary_key=True)
    id_random = db.Column(UUID(as_uuid=True), default=uuid.uuid4)
    pergunta = db.Column(db.Text, nullable=False)
    valor_score = db.Column(db.Integer, default=1)
    tema_estudo = db.Column(db.String(50))
    dificuldade = db.Column(db.String(10))
    opcao_a = db.Column(db.Text)
    opcao_b = db.Column(db.Text)
    opcao_c = db.Column(db.Text)
    opcao_d = db.Column(db.Text)
    resposta_correta = db.Column(db.String(1))
    explicacao = db.Column(db.Text)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'id_random': str(self.id_random),
            'pergunta': self.pergunta,
            'opcoes': {
                'A': self.opcao_a,
                'B': self.opcao_b,
                'C': self.opcao_c,
                'D': self.opcao_d
            },
            'dificuldade': self.dificuldade,
            'tema': self.tema_estudo
        }

class RespostaUsuario(db.Model):
    __tablename__ = 'respostas_usuarios'
    
    id = db.Column(db.Integer, primary_key=True)
    id_random = db.Column(UUID(as_uuid=True), default=uuid.uuid4)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    questao_id = db.Column(db.Integer, db.ForeignKey('cad_questoes.id_quest'), nullable=False)
    resposta = db.Column(db.String(1), nullable=False)
    pontuacao = db.Column(db.Integer, nullable=False)
    data_resposta = db.Column(db.DateTime, default=datetime.utcnow)
    
    usuario = db.relationship('Usuario', backref=db.backref('respostas', lazy=True))
    questao = db.relationship('Questao', backref=db.backref('respostas', lazy=True))

class Conquista(db.Model):
    __tablename__ = 'conquistas'
    
    id = db.Column(db.Integer, primary_key=True)
    id_random = db.Column(UUID(as_uuid=True), default=uuid.uuid4)
    nome = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    criterio = db.Column(db.Text, nullable=False)
    icone = db.Column(db.String(100))

class ConquistaUsuario(db.Model):
    __tablename__ = 'conquistas_usuarios'
    
    id = db.Column(db.Integer, primary_key=True)
    id_random = db.Column(UUID(as_uuid=True), default=uuid.uuid4)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    conquista_id = db.Column(db.Integer, db.ForeignKey('conquistas.id'), nullable=False)
    data_conquista = db.Column(db.DateTime, default=datetime.utcnow)
    
    usuario = db.relationship('Usuario', backref=db.backref('conquistas', lazy=True))
    conquista = db.relationship('Conquista', backref=db.backref('usuarios', lazy=True))

class PontuacaoMensal(db.Model):
    __tablename__ = 'pontuacoes_mensais'
    
    id = db.Column(db.Integer, primary_key=True)
    id_random = db.Column(UUID(as_uuid=True), default=uuid.uuid4)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    mes = db.Column(db.Integer, nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    pontuacao_total = db.Column(db.Integer, default=0)
    posicao_ranking = db.Column(db.Integer)
    
    usuario = db.relationship('Usuario', backref=db.backref('pontuacoes', lazy=True))
    
    __table_args__ = (
        db.UniqueConstraint('usuario_id', 'mes', 'ano', name='unique_pontuacao_mensal'),
    ) 