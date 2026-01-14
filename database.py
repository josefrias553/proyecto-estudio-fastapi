"""
Configuración de Base de Datos
==============================
Este archivo configura la conexión a PostgreSQL.
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

# URL de conexión a PostgreSQL desde .env
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL no está configurada en el archivo .env")

# Engine - Motor de conexión a PostgreSQL
engine = create_engine(DATABASE_URL)

# SessionLocal - Fábrica para crear sesiones de base de datos
# Una sesión es como una "conversación" con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base - Clase base para todos nuestros modelos ORM
# Todos los modelos heredarán de esta clase
Base = declarative_base()


def get_db():
    """
    Función que proporciona una sesión de base de datos.
    
    ¿Por qué usar yield?
    - Yield proporciona la sesión
    - FastAPI la usa en el endpoint
    - Después del yield, se ejecuta el finally
    - Esto asegura que la sesión siempre se cierre
    
    Es como un try-finally automático.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
