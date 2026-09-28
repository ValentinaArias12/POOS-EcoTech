from dominio.empleado import Empleado
from persistencia.conexion import abrir_conexion, marcador_sql

class EmpleadoDAO:
    
    @staticmethod
    def insertar(empleado):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marca = marcador_sql()
        sql = f"""
        INSERT INTO empleado (nombre, correo)
        VALUES ({marca}, {marca})
        """
        cursor.execute(sql, (empleado.nombre, empleado.correo))
        empleado.id = cursor.lastrowid
        conexion.commit()
        conexion.close()
        return empleado
    
    
    @staticmethod
    def buscar_por_id(id_empleado):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marca = marcador_sql()
        sql = f"""
        SELECT id, nombre, correo 
        FROM empleado WHERE id = {marca}
        """
        cursor.execute(sql, (id_empleado,))
        fila = cursor.fetchone()
        conexion.close()
        if fila is None:
            return None
        return EmpleadoDAO._fila_a_empleado(fila)

    @staticmethod
    def listar():
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT id, nombre, correo FROM empleado"
        )
        filas = cursor.fetchall()
        conexion.close()
        empleados = []
        for fila in filas:
            empleados.append(EmpleadoDAO._fila_a_empleado(fila))
        return empleados
    
    
    @staticmethod
    def _fila_a_empleado(fila):
        return Empleado(
            id=fila[0],
            nombre=fila[1],
            correo=fila[2]
        )

#19
    @staticmethod
    def buscar_por_correo(correo):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marca = marcador_sql()
        sql = f"""
        SELECT id, nombre, correo 
        FROM empleado WHERE correo = {marca}
        """
        cursor.execute(sql, (correo,))
        fila = cursor.fetchone()
        conexion.close()
        if fila is None:
            return None
        return EmpleadoDAO._fila_a_empleado(fila)


    @staticmethod
    def actualizar(empleado):
        """Actualiza un registro existente usando UPDATE parametrizado."""
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = (
                "UPDATE empleado "
                f"SET nombre = {marca}, correo = {marca} "
                f"WHERE id = {marca}"
            )
            cursor.execute(sql, (empleado.nombre, empleado.correo, empleado.id))
            conexion.commit()
            return cursor.rowcount > 0
        except Exception:
            if conexion:
                conexion.rollback()
            raise
        finally:
            if conexion:
                conexion.close()

    @staticmethod
    def eliminar(id_empleado):
        """Elimina un registro por ID usando DELETE parametrizado."""
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            marca = marcador_sql()
            sql = f"DELETE FROM empleado WHERE id = {marca}"
            cursor.execute(sql, (id_empleado,))
            conexion.commit()
            return cursor.rowcount > 0
        except Exception:
            if conexion:
                conexion.rollback()
            raise
        finally:
            if conexion:
                conexion.close()
#sirve para obtener todos los empleados de la base de datos daoS