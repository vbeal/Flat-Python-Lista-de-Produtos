
from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

CONN = 'sqlite:///database.db'

engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Produto(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True)
    produto = Column(String, nullable=False)
    preco = Column(Float, nullable=False)

    def __init__(self, produto, preco):
        self.produto = produto
        self.preco = preco

Base.metadata.create_all(engine)
