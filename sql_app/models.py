from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Word(Base):
    __tablename__ = 'words'

    id = Column(Integer, autoincrement=True, primary_key=True)
    word = Column(String, unique=True)
    lenght = Column(Integer, default=None)
