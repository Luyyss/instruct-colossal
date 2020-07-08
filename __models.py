# from sqlalchemy import Column, Integer, String, Text
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import create_engine

# Base = declarative_base()

# engine = create_engine('postgresql+psycopg2://olmpqxlstufibe:ae9db5deb023cb3598e7138915b4165b32269e44cb62def87f0ced1cd8ec5275@ec2-3-216-129-140.compute-1.amazonaws.com:5432/d2s5lto2hij18t', echo=True)

# class Estado(Base):
#     __tablename__ = 'tb_estado'

#     prefixo = Column(String(2), primary_key=True)
#     sigla = Column(String(2))

#     def __repr__(self):
#         return '<Estado {}>'.format(self.prefixo)


# class Cidade(Base):
#     __tablename__ = 'tb_cidade'

#     codigo = Column(String(7), primary_key=True)
#     nome = Column(String(100))

#     def __repr__(self):
#         return '<Cidade {}>'.format(self.codigo)


# class Feriado(Base):
#     __tablename__ = 'tb_feriado'

#     id = Column(Integer, primary_key=True)
#     name = Column(String(100))
#     poder = Column(String(1))
#     ano = Column(String(4), nullable=True)
#     mes = Column(String(2))
#     dia = Column(String(2))
#     tipo = Column(String(1))
#     local = Column(String(7), nullable=True)

#     def __repr__(self):
#         return '<Feriado {}>'.format(self.id)

# Base.metadata.create_all(engine)