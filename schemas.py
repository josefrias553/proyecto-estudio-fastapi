"""
Schemas Pydantic - Validación de Datos
======================================
Pydantic se encarga de validar automáticamente que los datos sean correctos.
Por ejemplo: que un email tenga formato válido, que los números sean positivos, etc.
"""
from pydantic import BaseModel, Field
from datetime import date
from decimal import Decimal


# SCHEMA DE ENTRADA - Lo que el cliente envía al crear una orden
class OrdenCreate(BaseModel):
    """
    Este schema define qué datos necesitamos para crear una orden.
    Pydantic validará automáticamente:
    - Que fecha sea una fecha válida
    - Que los IDs sean números enteros
    """
    fecha: date
    id_vendedor: int
    id_supermercado: int
    id_representante: int
    id_forma_pago: int


# SCHEMA DE SALIDA - Lo que la API devuelve al cliente
class OrdenResponse(BaseModel):
    """
    Este schema define cómo se verá la orden cuando la devolvamos.
    Incluye el ID que se generó automáticamente en la base de datos.
    """
    id_orden: int
    fecha: date
    id_vendedor: int
    id_supermercado: int
    id_representante: int
    id_forma_pago: int
    
    # Esta configuración permite que Pydantic lea datos de objetos SQLAlchemy
    class Config:
        from_attributes = True
