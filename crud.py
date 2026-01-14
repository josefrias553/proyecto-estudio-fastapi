"""
CRUD Operations - Operaciones de Base de Datos
==============================================
CRUD significa: Create, Read, Update, Delete
En este proyecto solo usamos Create y Read para mantenerlo simple.
"""
from sqlalchemy.orm import Session
import models
import schemas


def create_orden(db: Session, orden: schemas.OrdenCreate):
    """
    Crea una nueva orden en la base de datos.
    
    ¿Cómo funciona?
    1. Tomamos los datos validados por Pydantic
    2. Creamos un objeto SQLAlchemy (modelo)
    3. Lo agregamos a la sesión de base de datos
    4. Guardamos los cambios con commit()
    5. Refrescamos para obtener el ID generado
    """
    # Convertir el schema Pydantic a modelo SQLAlchemy
    db_orden = models.Orden(**orden.model_dump())
    
    # Agregar a la sesión (todavía no se guarda en la BD)
    db.add(db_orden)
    
    # Guardar en la base de datos
    db.commit()
    
    # Refrescar para obtener datos actualizados (como el ID auto-generado)
    db.refresh(db_orden)
    
    return db_orden


def get_ordenes(db: Session):
    """
    Obtiene todas las órdenes de la base de datos.
    
    ¿Qué es Session?
    Session es como una "conversación" con la base de datos.
    Nos permite hacer consultas, crear, actualizar o eliminar datos.
    
    ¿Qué hace query()?
    query() es el método de SQLAlchemy para consultar datos.
    .all() obtiene todos los registros.
    """
    return db.query(models.Orden).all()
