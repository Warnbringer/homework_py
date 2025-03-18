from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Строка подключения к базе данных
DATABASE_URL = "postgresql://postgres:5085@localhost:5432/QA"

# Создание объекта базы данных
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()


# Определение модели студента
class Student(Base):
    __tablename__ = 'user_id'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


# Создание всех таблиц
Base.metadata.create_all(engine)
