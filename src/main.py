from persistencia.crear_bd import crear_tablas
from dominio.empleado import Empleado
from persistencia.empleado_dao import EmpleadoDAO

if __name__ == "__main__":
    # 1. Crear tablas si no existen
    crear_tablas()

    # 2. Objeto nuevo en memoria (ID es None)
    empleado = Empleado(nombre="Ana Pérez", correo="ana@ecotech.cl")
    print("Antes de persistir -> ID:", empleado.id)

    # 3. Persistir objeto mediante el DAO
    EmpleadoDAO.insertar(empleado)

    # 4. Comprobar asignación de ID por la BD
    print("Después de persistir -> ID:", empleado.id)
    print("Empleado persistido:", empleado.mostrar_datos())