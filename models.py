"""
Modelos SQLAlchemy - Mapeo de Tablas
====================================
SQLAlchemy ORM (Object-Relational Mapping) permite trabajar con la base de datos
usando clases de Python en lugar de escribir SQL directamente.

Cada clase aquí representa una tabla en la base de datos.
"""
from sqlalchemy import Column, Integer, String, Numeric, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Estado(Base):
    """Tabla de estados/provincias"""
    __tablename__ = "estados"
    
    id_estado = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False, unique=True)
    
    # relationship() permite navegar entre tablas relacionadas
    ciudades = relationship("Ciudad", back_populates="estado")


class Ciudad(Base):
    """Tabla de ciudades"""
    __tablename__ = "ciudades"
    
    id_ciudad = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    id_estado = Column(Integer, ForeignKey("estados.id_estado"), nullable=False)
    
    estado = relationship("Estado", back_populates="ciudades")
    supermercados = relationship("Supermercado", back_populates="ciudad")


class Supermercado(Base):
    """Tabla de supermercados"""
    __tablename__ = "supermercados"
    
    id_supermercado = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150), nullable=False)
    id_ciudad = Column(Integer, ForeignKey("ciudades.id_ciudad"), nullable=False)
    
    ciudad = relationship("Ciudad", back_populates="supermercados")
    ordenes = relationship("Orden", back_populates="supermercado")


class Vendedor(Base):
    """Tabla de vendedores"""
    __tablename__ = "vendedores"
    
    id_vendedor = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150), nullable=False)
    email = Column(String(150), nullable=False, unique=True)
    
    ordenes = relationship("Orden", back_populates="vendedor")


class RepresentanteCompra(Base):
    """Tabla de representantes de compras"""
    __tablename__ = "representantes_compras"
    
    id_representante = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150), nullable=False)
    
    ordenes = relationship("Orden", back_populates="representante")


class Categoria(Base):
    """Tabla de categorías de productos"""
    __tablename__ = "categorias"
    
    id_categoria = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False, unique=True)
    
    productos = relationship("Producto", back_populates="categoria")


class Producto(Base):
    """Tabla de productos"""
    __tablename__ = "productos"
    
    id_producto = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150), nullable=False)
    presentacion = Column(String(100), nullable=False)
    precio_unitario_usd = Column(Numeric(10, 2), nullable=False)
    id_categoria = Column(Integer, ForeignKey("categorias.id_categoria"), nullable=False)
    
    categoria = relationship("Categoria", back_populates="productos")
    detalles_orden = relationship("DetalleOrden", back_populates="producto")


class FormaPago(Base):
    """Tabla de formas de pago"""
    __tablename__ = "formas_pago"
    
    id_forma_pago = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False, unique=True)
    
    ordenes = relationship("Orden", back_populates="forma_pago")


class Orden(Base):
    """
    Tabla principal - Órdenes de venta
    
    Esta es la tabla que usamos en el proyecto.
    Relaciona vendedores, supermercados, representantes y formas de pago.
    """
    __tablename__ = "ordenes"
    
    id_orden = Column(Integer, primary_key=True, index=True)
    fecha = Column(Date, nullable=False)
    id_vendedor = Column(Integer, ForeignKey("vendedores.id_vendedor"), nullable=False)
    id_supermercado = Column(Integer, ForeignKey("supermercados.id_supermercado"), nullable=False)
    id_representante = Column(Integer, ForeignKey("representantes_compras.id_representante"), nullable=False)
    id_forma_pago = Column(Integer, ForeignKey("formas_pago.id_forma_pago"), nullable=False)
    
    # Relaciones - permiten acceder a datos relacionados fácilmente
    vendedor = relationship("Vendedor", back_populates="ordenes")
    supermercado = relationship("Supermercado", back_populates="ordenes")
    representante = relationship("RepresentanteCompra", back_populates="ordenes")
    forma_pago = relationship("FormaPago", back_populates="ordenes")
    detalles = relationship("DetalleOrden", back_populates="orden")


class DetalleOrden(Base):
    """Tabla de detalles de cada orden (productos comprados)"""
    __tablename__ = "detalle_orden"
    
    id_detalle = Column(Integer, primary_key=True, index=True)
    id_orden = Column(Integer, ForeignKey("ordenes.id_orden"), nullable=False)
    id_producto = Column(Integer, ForeignKey("productos.id_producto"), nullable=False)
    cantidad_comprada = Column(Integer, nullable=False)
    valor_total_usd = Column(Numeric(12, 2), nullable=False)
    
    orden = relationship("Orden", back_populates="detalles")
    producto = relationship("Producto", back_populates="detalles_orden")
