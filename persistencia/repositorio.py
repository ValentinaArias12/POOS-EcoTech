import os
import sqlite3
from contextlib import closing
from pathlib import Path

from dotenv import load_dotenv

from dominio.empleado import Empleado


load_dotenv()


class EmpleadoRepositorio:
    def __init__(self, db_path: str | None = None) -> None:
        configured_path = db_path or os.getenv("DB_PATH", "data/ecotech.db")
        self.db_path = Path(configured_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._crear_tabla()

    def _conectar(self) -> sqlite3.Connection:
        return sqlite3.connect(self.db_path)

    def _conexion(self):
        return closing(self._conectar())

    def _crear_tabla(self) -> None:
        with self._conexion() as conexion:
            conexion.execute(
                """
                CREATE TABLE IF NOT EXISTS empleados (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    apellido TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    cargo TEXT NOT NULL
                )
                """
            )

    def guardar(self, empleado: Empleado) -> Empleado:
        with self._conexion() as conexion:
            cursor = conexion.execute(
                """
                INSERT INTO empleados (nombre, apellido, email, cargo)
                VALUES (?, ?, ?, ?)
                """,
                (empleado.nombre, empleado.apellido, empleado.email, empleado.cargo),
            )
            empleado.id = cursor.lastrowid
        return empleado

    def listar(self) -> list[Empleado]:
        with self._conexion() as conexion:
            filas = conexion.execute(
                "SELECT id, nombre, apellido, email, cargo FROM empleados ORDER BY id"
            ).fetchall()

        return [Empleado(*fila[1:], id=fila[0]) for fila in filas]
