<<<<<<< HEAD
from dominio.empleado import Empleado
from persistencia.conexion import abrir_conexion, marcador_sql, obtener_motor

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
    
    #sirve para obtener todos los empleados de la base de datos

    @staticmethod
    def buscar_por_id(id_empleado):
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marcador = marcador_sql()
        
        sql = f"""
        SELECT id, nombre, correo FROM empleado WHERE id = {marcador}
        """
        
        cursor.execute(sql, (id_empleado,))
        fila = cursor.fetchone()
        conexion.close()

        if fila is None:
                return None
        
        return Empleado(id=fila[0], nombre=fila[1], correo=fila[2])
=======
from dominio.empleado import Empleado, EmpleadoPlanta, EmpleadoContrata
from persistencia.conexion import abrir_conexion, marcador_sql

>>>>>>> ac8be7d (Implementa avances Ev2: nuevas entidades, DAO, CRUD y documentacion)

class EmpleadoDAO:
    @staticmethod
    def _valores_subtipo(empleado):
        return (
            getattr(empleado, "bono_anual", 0.0),
            getattr(empleado, "tarifa_hora", 0.0),
        )
<<<<<<< HEAD
        filas = cursor.fetchall()
        conexion.close()
        empleados = []
        for fila in filas:
            empleados.append(
                Empleado(
                    id=fila[0],
                    nombre=fila[1],
                    correo=fila[2]
                )
            )
        return empleados

    @staticmethod
    def actualizar(empleado):
=======

    @staticmethod
    def _fila_a_empleado(fila):
        (
            id_empleado, nombre, correo, telefono, fecha_inicio, salario_base,
            tipo, bono_anual, tarifa_hora, departamento_id
        ) = fila
        comunes = dict(
            id=id_empleado,
            nombre=nombre,
            correo=correo,
            telefono=telefono or "",
            fecha_inicio=str(fecha_inicio),
            salario_base=float(salario_base or 0),
            departamento_id=departamento_id,
        )
        if tipo == "PLANTA":
            return EmpleadoPlanta(**comunes, bono_anual=float(bono_anual or 0))
        if tipo == "CONTRATA":
            return EmpleadoContrata(**comunes, tarifa_hora=float(tarifa_hora or 0))
        return Empleado(**comunes)

    @staticmethod
    def insertar(empleado):
>>>>>>> ac8be7d (Implementa avances Ev2: nuevas entidades, DAO, CRUD y documentacion)
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            m = marcador_sql()
            bono, tarifa = EmpleadoDAO._valores_subtipo(empleado)
            sql = f"""
                INSERT INTO empleado
                (nombre, correo, telefono, fecha_inicio, salario_base, tipo,
                 bono_anual, tarifa_hora, departamento_id)
                VALUES ({m}, {m}, {m}, {m}, {m}, {m}, {m}, {m}, {m})
            """
            cursor.execute(sql, (
                empleado.nombre, empleado.correo, empleado.telefono,
                empleado.fecha_inicio, empleado.salario_base, empleado.TIPO,
                bono, tarifa, empleado.departamento_id,
            ))
            empleado.id = cursor.lastrowid
            conexion.commit()
            return empleado
        except Exception:
            if conexion:
                conexion.rollback()
            raise
        finally:
            if conexion:
                conexion.close()

    @staticmethod
    def buscar_por_id(id_empleado):
        conexion = abrir_conexion()
        try:
            cursor = conexion.cursor()
            m = marcador_sql()
            cursor.execute(
                f"SELECT id,nombre,correo,telefono,fecha_inicio,salario_base,tipo,bono_anual,tarifa_hora,departamento_id FROM empleado WHERE id={m}",
                (id_empleado,),
            )
<<<<<<< HEAD
            cursor.execute(
            sql,
                (
                empleado.nombre,
                empleado.correo,
                empleado.id
                )
            )
=======
            fila = cursor.fetchone()
            return None if fila is None else EmpleadoDAO._fila_a_empleado(fila)
        finally:
            conexion.close()

    @staticmethod
    def buscar_por_correo(correo):
        conexion = abrir_conexion()
        try:
            cursor = conexion.cursor()
            m = marcador_sql()
            cursor.execute(
                f"SELECT id,nombre,correo,telefono,fecha_inicio,salario_base,tipo,bono_anual,tarifa_hora,departamento_id FROM empleado WHERE correo={m}",
                (correo.strip().lower(),),
            )
            fila = cursor.fetchone()
            return None if fila is None else EmpleadoDAO._fila_a_empleado(fila)
        finally:
            conexion.close()

    @staticmethod
    def listar():
        conexion = abrir_conexion()
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT id,nombre,correo,telefono,fecha_inicio,salario_base,tipo,bono_anual,tarifa_hora,departamento_id FROM empleado ORDER BY id")
            return [EmpleadoDAO._fila_a_empleado(f) for f in cursor.fetchall()]
        finally:
            conexion.close()

    @staticmethod
    def actualizar(empleado):
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            m = marcador_sql()
            bono, tarifa = EmpleadoDAO._valores_subtipo(empleado)
            sql = (
                f"UPDATE empleado SET nombre={m}, correo={m}, telefono={m}, "
                f"fecha_inicio={m}, salario_base={m}, tipo={m}, bono_anual={m}, "
                f"tarifa_hora={m}, departamento_id={m} WHERE id={m}"
            )
            cursor.execute(sql, (
                empleado.nombre, empleado.correo, empleado.telefono,
                empleado.fecha_inicio, empleado.salario_base, empleado.TIPO,
                bono, tarifa, empleado.departamento_id, empleado.id,
            ))
>>>>>>> ac8be7d (Implementa avances Ev2: nuevas entidades, DAO, CRUD y documentacion)
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
<<<<<<< HEAD
        conexion = abrir_conexion()
        cursor = conexion.cursor()
        marca = marcador_sql()
        sql = (
            "DELETE FROM empleado "
            f"WHERE id = {marca}"
        )
        cursor.execute(sql, (id_empleado,))
        conexion.commit()
        eliminado = cursor.rowcount > 0
        conexion.close()
        return eliminado

=======
        conexion = None
        try:
            conexion = abrir_conexion()
            cursor = conexion.cursor()
            m = marcador_sql()
            cursor.execute(f"DELETE FROM empleado WHERE id={m}", (id_empleado,))
            conexion.commit()
            return cursor.rowcount > 0
        except Exception:
            if conexion:
                conexion.rollback()
            raise
        finally:
            if conexion:
                conexion.close()
>>>>>>> ac8be7d (Implementa avances Ev2: nuevas entidades, DAO, CRUD y documentacion)
