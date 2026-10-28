
from persistencia.crear_bd import crear_tablas
from persistencia.departamento_dao import DepartamentoDAO
from persistencia.empleado_dao import EmpleadoDAO
from dominio.departamento import Departamento
from dominio.empleado import Empleado


def cargar_departamentos():
    nombres = ["Tecnología", "Administración", "Recursos Humanos"]
    deptos_guardados = []
    for nombre_dept in nombres:
        existente = DepartamentoDAO.buscar_por_nombre(nombre_dept)
        if existente is not None:
            print(f"ℹ El departamento '{nombre_dept}' ya existe. Omitiendo...")
            deptos_guardados.append(existente)
        else:
            nuevo_depto = Departamento(nombre=nombre_dept)
            DepartamentoDAO.insertar(nuevo_depto)
            print(f"✔ Departamento '{nombre_dept}' creado exitosamente.")
            deptos_guardados.append(nuevo_depto)
    return deptos_guardados

def cargar_empleados(departamentos):
    datos = [
        ("Ana Torres", "ana@ecotech.example", departamentos[0]),
        ("Luis Pérez", "luis@ecotech.example", departamentos[0]),
        ("María González", "maria@ecotech.example", departamentos[1]),
        ("Pedro Ramírez", "pedro@ecotech.example", departamentos[1]),
        ("Carolina Soto", "carolina@ecotech.example", departamentos[2]),
        ("Jorge Díaz", "jorge@ecotech.example", departamentos[2]),
        ("Claudia Vega", "claudia@ecotech.example", departamentos[0]),
        ("Felipe Navarro", "felipe@ecotech.example", departamentos[1]),
        ("Daniela Rojas", "daniela@ecotech.example", departamentos[2]),
    ]
    empleado_admin = None
    for nombre, correo, depto in datos:
        existente = EmpleadoDAO.buscar_por_correo(correo)
        if existente is not None:
            print(f"ℹ Ya existe empleado: {correo}")
            if correo == "ana@ecotech.example":
                empleado_admin = existente
            continue
        

        depto_id = depto.id if hasattr(depto, "id") else depto
        empleado = Empleado(nombre=nombre, correo=correo, departamento_id=depto_id)
        EmpleadoDAO.insertar(empleado)
        print(f"✔ Creado empleado: {correo}")
        
        if correo == "ana@ecotech.example":
            empleado_admin = empleado
            
    return empleado_admin




def cargar_semillas():
    print(" Iniciando verificación e inserción de semillas...")
    crear_tablas() 
    departamentos = cargar_departamentos()
    print(" Carga de semillas completada.")

if __name__ == "__main__":
    cargar_semillas()