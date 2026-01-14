"""
API de Ventas de Lácteos - Proyecto de Aprendizaje
===================================================
Este es un proyecto educativo para aprender FastAPI y SQLAlchemy.
Maneja órdenes de ventas de productos lácteos.
"""
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
import crud
from database import engine, get_db

# Crear todas las tablas en la base de datos (si no existen)
models.Base.metadata.create_all(bind=engine)

# Crear la aplicación FastAPI
app = FastAPI(
    title="API FacuApi - Proyecto de Estudio",
    description="API educativa para practicar FastAPI y SQLAlchemy",
    version="1.0.0"
)


@app.get("/")
def root():
    """
    Endpoint raíz - mensaje de bienvenida
    """
    return {
        "mensaje": "API FacuApi",
        "proyecto": "Educativo - Práctica de FastAPI",
        "documentacion": "/docs"
    }


@app.post("/ordenes/", response_model=schemas.OrdenResponse)
def crear_orden(orden: schemas.OrdenCreate, db: Session = Depends(get_db)):
    """
    Endpoint POST - Crear una nueva orden
    
    ¿Cómo funciona FastAPI aquí?
    
    1. FastAPI recibe los datos JSON del cliente
    2. Pydantic valida que los datos cumplan con 'OrdenCreate'
    3. Depends(get_db) inyecta automáticamente una sesión de BD
    4. Llamamos a la función CRUD para guardar en la BD
    5. FastAPI convierte el resultado a JSON y lo devuelve
    
    Si algo falla, HTTPException devuelve un error al cliente.
    """
    try:
        return crud.create_orden(db=db, orden=orden)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error al crear orden: {str(e)}")


@app.get("/ordenes/", response_model=List[schemas.OrdenResponse])
def listar_ordenes(db: Session = Depends(get_db)):
    """
    Endpoint GET - Obtener todas las órdenes
    
    ¿Qué es Depends(get_db)?
    
    FastAPI usa 'Depends' para inyección de dependencias.
    get_db() es una función que:
    - Abre una conexión a la base de datos
    - La proporciona a nuestro endpoint
    - La cierra automáticamente al terminar
    
    Esto es útil porque no tenemos que recordar cerrar la conexión.
    """
    return crud.get_ordenes(db=db)
