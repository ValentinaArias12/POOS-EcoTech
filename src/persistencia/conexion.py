import os
import sqlite3
from dotenv import load_dotenv

load_dotenv()


def obtener_motor() -> str:
    return os.getenv("DB_ENGINE", "sqlite").strip().lower()


def abrir_conexion():
    motor = obtener_motor()
    if motor == "sqlite":
        conexion = sqlite3.connect(os.getenv("DB_NAME", "ecotech.db"))
        conexion.execute("PRAGMA foreign_keys = ON")
        return conexion

    if motor == "mysql":
        try:
            import pymysql
        except ImportError as exc:
            raise RuntimeError(
                "PyMySQL no está instalado. Ejecuta: pip install -r requirements.txt"
            ) from exc
        return pymysql.connect(
            host=os.getenv("DB_HOST", "localhost"),
            port=int(os.getenv("DB_PORT", "3306")),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            charset="utf8mb4",
        )

    raise ValueError(f"Motor no soportado: {motor}")

<<<<<<< HEAD
def marcador_sql():
    if obtener_motor() == "sqlite":
        return "?"
<<<<<<< HEAD
    return "%s"
    
=======
    return "%s"
>>>>>>> 7f9494a9836c597f7b1abb44348cf2df6a7a8b28
=======

def marcador_sql() -> str:
    return "?" if obtener_motor() == "sqlite" else "%s"
>>>>>>> ac8be7d (Implementa avances Ev2: nuevas entidades, DAO, CRUD y documentacion)
