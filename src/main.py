from persistencia.crear_bd import crear_tablas
from dominio.empleado import Empleado
from dominio.departamento import Departamento
from persistencia.empleado_dao import EmpleadoDAO
from persistencia.departamento_dao import DepartamentoDAO

if __name__ == "__main__":
    # Creamos las tablas
    crear_tablas()

    
    empleado = Empleado(nombre="Ana Pérez", correo="ana@ecotech.cl")
    departamento = Departamento(nombre="Desarrollo de Software")

    print("--- sin id ---")
    print(f"Empleado     -> ID: {empleado.id} | Nombre: {empleado.nombre}")
    print(f"Departamento -> ID: {departamento.id} | Nombre: {departamento.nombre}")

    #Insertamos
    EmpleadoDAO.insertar(empleado)
    DepartamentoDAO.insertar(departamento)

    print("\n--- con id ---")
    print(f"Empleado     -> ID: {empleado.id} | Registro: {empleado}")
    print(f"Departamento -> ID: {departamento.id} | Nombre: {departamento.nombre}")

    #READ 
    encontrado_id = EmpleadoDAO.buscar_por_id(empleado.id)
    print("\n--- Buscar por ID ---")
    print("Encontrado por ID:", encontrado_id)

    por_correo = EmpleadoDAO.buscar_por_correo(empleado.correo)
    print("\n--- Buscar por Correo ---")
    print("Encontrado por Correo:", por_correo)

    # UPDATE
    print("\n--- Actualización ---")
    empleado.correo = "ana.perez.nuevo@ecotech.cl"
    try:
        if EmpleadoDAO.actualizar(empleado):
            print("Empleado actualizado correctamente en la BD.")
        else:
            print("No se encontró el registro para actualizar.")
    except Exception:
        print("Ocurrió un error inesperado al intentar actualizar.")

    #DELETE y prueba de ID inexistente
    print("\n--- Eliminación ---")
    try:
        # Eliminamos registro existente
        if EmpleadoDAO.eliminar(empleado.id):
            print(f"Empleado con ID {empleado.id} eliminado con éxito.")
        else:
            print("No se encontró el empleado.")

        # Caso B: Probar ID inexistente
        id_inexistente = 99999
        if EmpleadoDAO.eliminar(id_inexistente):
            print(f"Empleado con ID {id_inexistente} eliminado.")
        else:
            print(f"El ID {id_inexistente} no existe en la BD (Resultado normal, retorna False).")
    except Exception:
        print("Ocurrió un error inesperado de persistencia al intentar eliminar.")

    #Listado final
    print("\n--- Listado Completo de Empleados ---")
    empleados = EmpleadoDAO.listar()
    if empleados:
        for emp in empleados:
            print(emp)
    else:
        print("No hay empleados registrados en la base de datos.")
    
    