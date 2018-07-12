from app import db
from sqlalchemy.orm import backref

# profhabilidades = db.Table("profissionalHabilidade",
#     db.Column('id_profissional', db.Integer, db.ForeignKey('profissional.id'), primary_key=True),
#     db.Column('id_habilidade', db.Integer, db.ForeignKey('habilidade.id'), primary_key=True)
# )

refprofissionais = db.Table("reformaProfissional",
    db.Column('id_reforma', db.Integer, db.ForeignKey('reforma.id', ondelete='CASCADE'), primary_key=True),
    db.Column('id_profissional', db.Integer, db.ForeignKey('profissional.id', ondelete='CASCADE'), primary_key=True)
)

class Profissional(db.Model):
    __tablename__ = "profissional"

    id = db.Column(db.Integer, primary_key=True)
    id_pessoa = db.Column(db.Integer, db.ForeignKey('pessoa.id', ondelete='CASCADE'), unique=True, nullable=False)
    #id_areaAtuacao = db.Column(db.Integer)

    reformas = db.relationship('Reforma', secondary=refprofissionais, lazy='subquery', backref=backref('profissionais', passive_deletes=True))
    pessoa = db.relationship('Pessoa', backref=backref('profissional', passive_deletes=True), uselist=False, lazy='joined')

    # habilidades = db.relationship('Habilidade', secondary=profhabilidades, lazy='subquery', backref='profissional')
    # negociacoes = db.relationship('NegociacaoPreco', backref='profissional')
    # conversas = db.relationship('Conversa',backref='profissional')

    def __init__(self, id_pessoa):#, id_areaAtuacao):
        self.id_pessoa = id_pessoa
        #self.id_areaAtuacao = id_areaAtuacao

    def __repr__(self):
        return "<Profissional %r>" % self.id_pessoa
