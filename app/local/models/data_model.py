from sqlalchemy import Column, Integer, Text,create_engine
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('postgresql://postgres:89080620743@localhost:5432/parsing')
# Определение класса Parsing_Data и его структуры столбцов
class Parsing_Data(Base):
    __tablename__ = 'ParsingData'
    id = db.Column(Integer, primary_key=True)
    name = db.Column(db.Text)
    keywords = db.Column(db.Text)
    base_url = db.Column(db.Text)
    url = db.Column(db.Text)
# создание таблицы в бд
Base.metadata.create_all(engine)