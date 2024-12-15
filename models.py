from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

CONN = 'sqlite:///database.db'

engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Produto(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True)
    produto = Column(String, nullable=False)
    price = Column(Float, nullable=False)

    Base.metadata.create_all(engine)