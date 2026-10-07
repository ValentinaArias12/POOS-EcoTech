from dominio.registro_tiempo import RegistroTiempo
from persistencia.conexion import abrir_conexion, marcador_sql


class RegistroTiempoDAO:
    @staticmethod
    def _fila_a_registro(fila):
        return RegistroTiempo(
            id=fila[0], fecha=str(fila[1]), horas=float(fila[2]), descripcion=fila[3],
            empleado_id=fila[4], proyecto_id=fila[5]
        )

    @staticmethod
    def insertar(registro):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            m = marcador_sql()
            cursor.execute(
                f"INSERT INTO registro_tiempo (fecha,horas,descripcion,empleado_id,proyecto_id) VALUES ({m},{m},{m},{m},{m})",
                (registro.fecha, registro.horas, registro.descripcion, registro.empleado_id, registro.proyecto_id),
            )
            registro.id = cursor.lastrowid
            conexion.commit()
            return registro
        except Exception:
            if conexion:
                conexion.rollback()
            raise
        finally:
            if conexion:
                conexion.close()

    @staticmethod
    def buscar_por_id(id_registro):
        conexion = abrir_conexion()
        try:
            cursor = conexion.cursor()
            m = marcador_sql()
            cursor.execute(f"SELECT id,fecha,horas,descripcion,empleado_id,proyecto_id FROM registro_tiempo WHERE id={m}", (id_registro,))
            fila = cursor.fetchone()
            return None if fila is None else RegistroTiempoDAO._fila_a_registro(fila)
        finally:
            conexion.close()

    @staticmethod
    def listar():
        conexion = abrir_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT id,fecha,horas,descripcion,empleado_id,proyecto_id FROM registro_tiempo ORDER BY fecha DESC,id DESC")
            return [RegistroTiempoDAO._fila_a_registro(f) for f in cursor.fetchall()]
        finally:
            conexion.close()

    @staticmethod
    def actualizar(registro):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            m = marcador_sql()
            cursor.execute(
                f"UPDATE registro_tiempo SET fecha={m},horas={m},descripcion={m},empleado_id={m},proyecto_id={m} WHERE id={m}",
                (registro.fecha, registro.horas, registro.descripcion, registro.empleado_id, registro.proyecto_id, registro.id),
            )
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
    def eliminar(id_registro):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            m = marcador_sql()
            cursor.execute(f"DELETE FROM registro_tiempo WHERE id={m}", (id_registro,))
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
    def horas_por_proyecto(id_proyecto):
        conexion = abrir_conexion()
        try:
            cursor = conexion.cursor()
            m = marcador_sql()
            cursor.execute(f"SELECT COALESCE(SUM(horas),0) FROM registro_tiempo WHERE proyecto_id={m}", (id_proyecto,))
            return float(cursor.fetchone()[0] or 0)
        finally:
            conexion.close()
