# API Ventas Lácteos 🥛

Proyecto educativo usando FastAPI + SQLAlchemy + PostgreSQL

## 📋 Requisitos Previos

- Python 3.10+
- Docker Desktop instalado y corriendo

## ⚡ Pasos para Ejecutar

### 1. Crear y Levantar la Base de Datos PostgreSQL con Docker

```bash
docker run --name postgres-supermercado \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=supermercado \
  -p 5432:5432 \
  -d postgres
```

**Verificar que el contenedor está corriendo:**
```bash
docker ps
```

**Si necesitas detener el contenedor:**
```bash
docker stop postgres-supermercado
```

**Para iniciarlo de nuevo:**
```bash
docker start postgres-supermercado
```

### 2. Conectar con DBeaver y Crear las Tablas

**Conectar a PostgreSQL:**
1. Abre DBeaver
2. Nueva Conexión → PostgreSQL
3. Configuración:
   - **Host:** localhost
   - **Puerto:** 5432
   - **Base de datos:** supermercado
   - **Usuario:** postgres
   - **Contraseña:** postgres
4. Test Connection → Finish

**Ejecutar el script SQL para crear las tablas:**
1. En DBeaver, click derecho en la conexión "supermercado"
2. SQL Editor → New SQL Script
3. Abre el archivo `create.sql` (está en la carpeta del proyecto)
4. Copia todo el contenido de `create.sql`
5. Pega en el editor SQL de DBeaver
6. Click en **Execute SQL Script** (ícono de "play" o Ctrl+Alt+X)
7. ✅ Verás que se crean las 10 tablas

**Verificar:**
- En el panel izquierdo de DBeaver, expande: Databases → supermercado → Schemas → public → Tables
- Deberías ver: estados, ciudades, supermercados, vendedores, representantes_compras, categorias, productos, formas_pago, ordenes, detalle_orden

### 3. Configurar Variables de Entorno

El archivo `.env` ya está configurado con:
```
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/supermercado
```

Si cambiaste la contraseña en Docker, edita el archivo `.env` con tus credenciales.

### 4. Instalar Dependencias de Python

```bash
pip install -r requirements.txt
```

**Importante:** Esto instalará `psycopg2-binary` que es necesario para conectar Python con PostgreSQL.

### 5. Ejecutar la API

```bash
uvicorn main:app --reload
```

✅ La API estará disponible en: **http://localhost:8000**

### 6. Ver Documentación Interactiva

Abre en tu navegador: **http://localhost:8000/docs**

Aquí puedes probar los endpoints directamente.

## 📊 Cargar Datos del CSV (Opcional)

Tienes el archivo `ventas_lacteos_2024.csv` con los datos.

**Usando DBeaver:**
1. Ya deberías estar conectado (paso 2)
2. Navega a la tabla donde quieres importar datos
3. Click derecho en la tabla → Import Data
4. Seleccionar el archivo CSV
5. Mapear las columnas correctamente
6. Importar

**Nota:** Primero necesitas tener datos en las tablas relacionadas (estados, ciudades, vendedores, etc.) antes de importar órdenes.

## 📝 Endpoints Disponibles

- **POST** `/ordenes/` - Crear una nueva orden
- **GET** `/ordenes/` - Listar todas las órdenes

Prueba los endpoints en: http://localhost:8000/docs

## 🗄️ Estructura de la Base de Datos

El esquema completo está definido en `create.sql`:
- Estados
- Ciudades
- Supermercados
- Vendedores
- Representantes de Compras
- Categorías
- Productos
- Formas de Pago
- **Órdenes** (tabla principal que usamos)
- Detalle de Órdenes

## ⚠️ Notas Importantes

- Este es un **proyecto educativo**, no productivo
- Las tablas se crean ejecutando `create.sql` en DBeaver (paso 2)
- La primera vez que ejecutes, las tablas estarán vacías (sin datos)
- Docker debe estar corriendo para que funcione PostgreSQL
- Puedes importar el CSV después de crear las tablas

## 🛑 Solución de Problemas

**Error: "could not translate host name"**
→ Asegúrate que Docker esté corriendo y el contenedor postgres-supermercado esté activo

**Error: "password authentication failed"**
→ Verifica que la contraseña en `.env` coincida con la de Docker (por defecto: postgres)

**Error: "database does not exist"**
→ Verifica que creaste el contenedor con `-e POSTGRES_DB=supermercado`
