from unicodedata import numeric
from sqlalchemy import create_engine, Column, Integer, String, VARCHAR, Numeric, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

user ='postgres'
password = '2509'
host = 'localhost'
port = '5432'
bd = 'aula_teste'

engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{bd}', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Heroi(Base):
    __tablename__ = 'heroi'
    
    id = Column(Integer, primary_key=True)
    nome = Column(VARCHAR(255))
    nivel = Column(Numeric)
    forca = Column(Numeric)
    defesa = Column(Numeric)
    mana = Column(Numeric)
    moedas = Column(Numeric)
    xp = Column(Numeric)

    #contacts = relationship('Contato', backref='users')
    
    def __repr__(self):
        return f'Usuario(nome={self.nome})'
    
class Monstro(Base):
    __tablename__ = 'monstro'
    id = Column(Integer, primary_key=True)
    nome = Column(VARCHAR(255))
    nivel = Column(Numeric)
    forca = Column(Numeric)
    defesa = Column(Numeric)
    mana = Column(Numeric)
    tipo = Column(VARCHAR(20))
    moedas_recompensa = Column(Numeric)
    xp_recompensa = Column(Numeric)
    #boss = Boolean ( )
    #agressivo = Boolean ()



#    user_id = Column(Integer, ForeignKey('users.id'))
 #   user = relationship(Usuario)

    def __repr__(self):
        return f'Contato(telefone= {self.nome}, user={self.defesa})'
Base.metadata.create_all(engine)

h1 = Usuario(nome='Hector', nivel = 21, forca=40, defesa=20, mana = 20, moedas = 23, xp = 14)
#u3 = Usuario(nome='Tulio')
#u4 = Usuario(nome='Victoria')
#session.add_all([u2, u3, u4])
#session.commit()

#query = session.query(Usuario).filter(Usuario.nome=='Gabriel')
#print(query)

#c1 = Contato(telefone='123457', user_id=query.id)
#c2 = Contato(telefone='987654', user=query)

#session.add_all([c1, c2])
#session.commit()
#query2 = session.query(Contato).first()
#print(query2.user.contacts[1].telefone)