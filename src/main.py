from persistencia.crear_bd import crear_tablas
from dominio.empleado import Empleado
from dominio.departamento import Departamento
from persistencia.empleado_dao import EmpleadoDAO
from persistencia.departamento_dao import DepartamentoDAO

if __name__ == "__main__":
    crear_tablas()

    empleado = Empleado(nombre="Ana Pérez", correo="ana@ecotech.cl")
    departamento = Departamento(nombre="Desarrollo de Software")

    print("--- Estado ANTES de persistir ---")
    print(f"Empleado -> ID: {empleado.id} | Nombre: {empleado.nombre}")
    print(f"Departamento -> ID: {departamento.id} | Nombre: {departamento.nombre}")

    # Solicitar la persistencia a través de sus respectivos DAO
    EmpleadoDAO.insertar(empleado)
    DepartamentoDAO.insertar(departamento)

    print("\n--- Estado DESPUÉS de persistir ---")
    print(f"Empleado -> ID: {empleado.id} | Registro: {empleado.mostrar_datos()}")
    print(f"Departamento -> ID: {departamento.id} | Registro: {departamento.mostrar_datos()}")