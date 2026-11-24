# app/database.py
from sqlalchemy import create_engine, Column, Integer, Text, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from datetime import datetime
import json
import os

# Указываем путь к базе данных в корне проекта (на уровень выше папки app)
# Если база данных должна создаться прямо в папке app, оставь 'sqlite:///matrix_project.db'
db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'matrix_project.db')
engine = create_engine(f'sqlite:///{db_path}', echo=False)

Base = declarative_base()

class Matrix(Base):
    __tablename__ = 'matrices'
    id = Column(Integer, primary_key=True)
    rows = Column(Integer, nullable=False)
    cols = Column(Integer, nullable=False)
    data = Column(Text, nullable=False) # Храним как JSON строку
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Связь 1 к 1 с результатом
    result = relationship("Result", back_populates="matrix", uselist=False)

class Result(Base):
    __tablename__ = 'results'
    id = Column(Integer, primary_key=True)
    matrix_id = Column(Integer, ForeignKey('matrices.id'))
    result_data = Column(Text, nullable=False) # Результат по столбцам (JSON)
    
    matrix = relationship("Matrix", back_populates="result")

# Создаем таблицы
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def get_session():
    return Session()