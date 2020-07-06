from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

engine = create_engine('postgresql+psycopg2://jjsnpzvghssord:989264f977fd75081cfd4f7d619f531f5c20120a71ad28b513baffe40172326a@ec2-3-208-50-226.compute-1.amazonaws.com:5432/dcbcf4l61o8l2n', echo=True)

class Estado(Base):
    __tablename__ = 'tb_estado'
    # __table_args__ = {"schema": "example"}

    id = Column(Integer, primary_key=True)
    prefixo = Column(String(7))
    nome = Column(String(100))

    # def __init__(self, url, result_all, result_no_stop_words):
    #     self.url = url
    #     self.result_all = result_all
    #     self.result_no_stop_words = result_no_stop_words

    def __repr__(self):
        return '<Estado {}>'.format(self.id)

class Cidade(Base):
    __tablename__ = 'tb_cidade'

    codigo = Column(String(7), primary_key=True)
    nome = Column(String(100))

    def __repr__(self):
        return '<Cidade {}>'.format(self.codigo)


class Feriado(Base):
    __tablename__ = 'tb_feriado'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    poder = Column(String(1))
    ano = Column(String(4), nullable=True)
    mes = Column(String(2))
    dia = Column(String(2))
    tipo = Column(String(1))
    local = Column(String(1), nullable=True)

    def __repr__(self):
        return '<Feriado {}>'.format(self.id)

Base.metadata.create_all(engine)