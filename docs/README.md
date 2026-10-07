# EcoTech

Aplicación de gestión de empleados, departamentos, proyectos y horas
trabajadas, organizada en capas de dominio y persistencia.

## Requisitos

- Python 3.10 o superior.
- Dependencias de `requirements.txt`.
- SQLite por defecto o una instancia MySQL configurada mediante `.env`.

Instalación:

```powershell
python -m pip install -r requirements.txt
```

## Configuración

Copia `.env.example` como `.env` y ajusta la configuración de la base de
datos. `.env` es local y no debe versionarse.

SQLite es la opción predeterminada:

```dotenv
DB_ENGINE=sqlite
DB_NAME=ecotech.db
```

## Ejecución

Desde la raíz del proyecto:

```powershell
python src/main.py
```

El menú permite administrar departamentos, empleados, proyectos y registros
de tiempo, incluyendo búsquedas, actualizaciones, eliminaciones y asignación
de empleados a proyectos.

## Estructura

- `src/dominio`: entidades y reglas de negocio.
- `src/persistencia`: conexión, creación de tablas y DAO parametrizados.
- `src/main.py`: menú interactivo y validaciones de entrada.
