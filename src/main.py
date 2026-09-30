
from persistencia.crear_bd import crear_tablas
from dominio.empleado import Empleado
from dominio.departamento import Departamento
from persistencia.empleado_dao import EmpleadoDAO
from persistencia.departamento_dao import DepartamentoDAO


def solicitar_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion < 0 or opcion > 5:
                print("Opción fuera de rango.")
                continue
            return opcion
        except ValueError:
            print("Debe ingresar un número.")
def registrar_empleado():
    nombre = input("Nombre: ").strip()
    correo = input("Correo: ").strip()
    empleado = Empleado(nombre, correo)
    try:
        EmpleadoDAO.insertar(empleado)
        print("Empleado registrado correctamente.")
    except Exception:
        print("No fue posible registrar el empleado.")

def listar_empleados():
    # Lógica para listar consumiendo EmpleadoDAO.listar()
    pass

def menu_empleado():
    while True:
        print("\n--- Menú ---")
        print("1. Registrar empleado")
        print("2. Listar empleados")
        print("0. Salir")
        
        opcion = solicitar_opcion()
        
        if opcion == 1:
            registrar_empleado()
        elif opcion == 2:
            listar_empleados()
        elif opcion == 0:
            print("Saliendo del programa.")
            break

