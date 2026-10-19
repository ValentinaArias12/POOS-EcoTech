from persistencia.departamento_dao import DepartamentoDAO
from persistencia.empleado_dao import EmpleadoDAO
from dominio.departamento import Departamento
from dominio.empleado import Empleado

def cargar_departamentos():
    datos = [
        ("Tecnología"),
        ("Recursos Humanos"),
        ("Finanzas"),
        ("Marketing"),
        ("Operaciones")
    ]
    departamentos = []
    for nombre in datos:
        existente = DepartamentoDAO.buscar_por_id(id)
        if existente is not None:
            print(f"Ya existe departamento: {id}")
            departamentos.append(existente)
            continue
        depto = Departamento(nombre)
        DepartamentoDAO.insertar(depto)
        print(f"Creado departamento: {nombre}")
        departamentos.append(depto)
    return departamentos

def cargar_empleados(departamentos):
    datos = [
        ("Ana Torres", "ana@ecotech.example", departamentos[0]),
        ("Luis Pérez", "luis@ecotech.example", departamentos[0]),
        ("María González", "maria@ecotech.example", departamentos[1]),
        ("Pedro Ramírez", "pedro@ecotech.example", departamentos[1]),
        ("Carolina Soto", "carolina@ecotech.example", departamentos[2]),
        ("Jorge Díaz", "jorge@ecotech.example", departamentos[2]),
        ("Valeria Campos", "valeria@ecotech.example", departamentos[3]),
        ("Andrés Herrera", "andres@ecotech.example", departamentos[3]),
        ("Sofía Morales", "sofia@ecotech.example", departamentos[4]),
        ("Ricardo Fuentes", "ricardo@ecotech.example", departamentos[4]),
        ("Claudia Vega", "claudia@ecotech.example", departamentos[0]),
        ("Felipe Navarro", "felipe@ecotech.example", departamentos[1]),
        ("Daniela Rojas", "daniela@ecotech.example", departamentos[2]),
        ("Héctor Silva", "hector@ecotech.example", departamentos[3]),
        ("Isabel Contreras", "isabel@ecotech.example", departamentos[4]),
        ("Tomás Castillo", "tomas@ecotech.example", departamentos[0]),
        ("Gabriela Flores", "gabriela@ecotech.example", departamentos[1]),
        ("Rodrigo Pino", "rodrigo@ecotech.example", departamentos[2]),
        ("Natalia Reyes", "natalia@ecotech.example", departamentos[3]),
        ("Francisco Bravo", "francisco@ecotech.example", departamentos[4]),
    ]
    for nombre, correo, depto in datos:
        existente = EmpleadoDAO.buscar_por_correo(correo)
        if existente is not None:
            print(f"Ya existe empleado: {correo}")
            continue
        empleado = Empleado(nombre, correo, depto)
        EmpleadoDAO.insertar(empleado)
        print(f"Creado empleado: {correo}")


def cargar_semillas():
    departamentos = cargar_departamentos()
    cargar_empleados(departamentos)

