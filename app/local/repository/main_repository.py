from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from app.local.models import data_model
from app.local.models.data_model import Parsing_Data
Base = declarative_base()

engine = create_engine('postgresql://postgres:89080620743@localhost:5432/parsing')
connection = engine.connect()
metadata = db.MetaData()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Создание таблицы в базе данных!
Base.metadata.create_all(engine)
# проверка существует ли ссылка в базне данных по базовому URL!
def check_existing_link(session: Session, link: str) -> Parsing_Data:
    existing_link = session.query(Parsing_Data).filter(Parsing_Data.url == link).first()
    return existing_link
#  Создает новую запись Parsing_Data, если ссылка не существует в базе данных!
def create_new_link(session: Session, base_url: str, link: str) -> None:
    existing_link = check_existing_link(session, link)
    if existing_link is None:
        new_link = Parsing_Data(name="Название ссылки", keywords="Ключевые слова", base_url=base_url, url=link)
        session.add(new_link)

