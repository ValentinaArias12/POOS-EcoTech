from dominio.usuario import Usuario
from persistencia.conexion import abrir_conexion, marcador_sql

class UsuarioDAO:
    @staticmethod
    def _fila_a_usuario(fila) -> Usuario:
        return Usuario(
            id=fila[0],
            nombre_usuario=fila[1],
            password_hash=fila[2],
            empleado_id=fila[3],
            rol=fila[4],
        )

    @staticmethod
    def insertar(usuario: Usuario) -> int:
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"""
                INSERT INTO usuario (nombre_usuario, password_hash, empleado_id, rol) 
                VALUES ({marca}, {marca}, {marca}, {marca})
            """
            cursor.execute(
                sql,
                (
                    usuario.nombre_usuario,
                    usuario.password_hash,
                    usuario.empleado_id,
                    usuario.rol,
                ),
            )
            conexion.commit()
            usuario.id = cursor.lastrowid
            return usuario.id
        except Exception:
            if conexion:
                conexion.rollback()
            raise
        finally:
            if conexion:
                conexion.close()

    @staticmethod
    def buscar_por_nombre(nombre_usuario: str) -> Usuario | None:
        conexion = abrir_conexion()
        try:
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"SELECT id, nombre_usuario, password_hash, empleado_id, rol FROM usuario WHERE nombre_usuario = {marca}"
            cursor.execute(sql, (nombre_usuario,))
            fila = cursor.fetchone()
            return None if fila is None else UsuarioDAO._fila_a_usuario(fila)
        finally:
            conexion.close()

    @staticmethod
    def buscar_por_empleado(empleado_id: int) -> Usuario | None:
        conexion = abrir_conexion()
        try:
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"SELECT id, nombre_usuario, password_hash, empleado_id, rol FROM usuario WHERE empleado_id = {marca}"
            cursor.execute(sql, (empleado_id,))
            fila = cursor.fetchone()
            return None if fila is None else UsuarioDAO._fila_a_usuario(fila)
        finally:
            conexion.close()

    @staticmethod
    def buscar_por_id(id_usuario: int) -> Usuario | None:
        conexion = abrir_conexion()
        try:
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"SELECT id, nombre_usuario, password_hash, empleado_id, rol FROM usuario WHERE id = {marca}"
            cursor.execute(sql, (id_usuario,))
            fila = cursor.fetchone()
            return None if fila is None else UsuarioDAO._fila_a_usuario(fila)
        finally:
            conexion.close()