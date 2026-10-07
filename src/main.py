
from persistencia.crear_bd import crear_tablas
from persistencia.departamento_dao import DepartamentoDAO
from persistencia.empleado_dao import EmpleadoDAO
from persistencia.proyecto_dao import ProyectoDAO
from persistencia.registro_tiempo_dao import RegistroTiempoDAO
from dominio.departamento import Departamento
from dominio.empleado import Empleado, EmpleadoPlanta, EmpleadoContrata
from dominio.proyecto import Proyecto
from dominio.registro_tiempo import RegistroTiempo


def pedir_entero(mensaje, permitir_vacio=False):
    while True:
        valor = input(mensaje).strip()
        if permitir_vacio and not valor:
            return None
        try:
            return int(valor)
        except ValueError:
            print("Debe ingresar un número entero válido.")


def pedir_float(mensaje, minimo=0.0, permitir_vacio=False):
    while True:
        valor = input(mensaje).strip()
        if permitir_vacio and not valor:
            return None
        try:
            numero = float(valor)
            if numero < minimo:
                print(f"El valor debe ser mayor o igual a {minimo}.")
                continue
            return numero
        except ValueError:
            print("Debe ingresar un número válido.")


def listar_departamentos():
    items = DepartamentoDAO.listar()
    if not items:
        print("No hay departamentos registrados.")
        return
    for item in items:
        print(item)


def menu_departamentos():
    while True:
        print("\n--- DEPARTAMENTOS ---")
        print("1. Crear")
        print("2. Listar")
        print("3. Actualizar")
        print("4. Eliminar")
        print("0. Volver")
        op = input("Opción: ").strip()
        try:
            if op == "1":
                dep = Departamento(input("Nombre: "))
                DepartamentoDAO.insertar(dep)
                print(f"Departamento creado con ID {dep.id}.")
            elif op == "2":
                listar_departamentos()
            elif op == "3":
                id_dep = pedir_entero("ID: ")
                dep = DepartamentoDAO.buscar_por_id(id_dep)
                if dep is None:
                    print("Departamento no encontrado.")
                    continue
                dep.nombre = input(f"Nuevo nombre [{dep.nombre}]: ").strip() or dep.nombre
                print("Actualizado." if DepartamentoDAO.actualizar(dep) else "Sin cambios.")
            elif op == "4":
                id_dep = pedir_entero("ID: ")
                print("Eliminado." if DepartamentoDAO.eliminar(id_dep) else "No encontrado.")
            elif op == "0":
                return
            else:
                print("Opción no válida.")
        except ValueError as exc:
            print(f"Validación: {exc}")
        except Exception:
            print("No fue posible completar la operación de departamento.")


def crear_empleado_desde_entrada():
    nombre = input("Nombre: ")
    correo = input("Correo: ")
    telefono = input("Teléfono (opcional): ")
    salario = pedir_float("Salario base: ", minimo=0)
    dep_id = pedir_entero("ID departamento (Enter = sin departamento): ", permitir_vacio=True)
    tipo = input("Tipo [1=Base, 2=Planta, 3=Contrata]: ").strip()
    comunes = dict(nombre=nombre, correo=correo, telefono=telefono, salario_base=salario, departamento_id=dep_id)
    if tipo == "2":
        return EmpleadoPlanta(**comunes, bono_anual=pedir_float("Bono anual: ", minimo=0))
    if tipo == "3":
        return EmpleadoContrata(**comunes, tarifa_hora=pedir_float("Tarifa hora: ", minimo=0))
    return Empleado(**comunes)


def menu_empleados():
    while True:
        print("\n--- EMPLEADOS ---")
        print("1. Registrar")
        print("2. Listar")
        print("3. Buscar por ID")
        print("4. Buscar por correo")
        print("5. Actualizar correo/departamento")
        print("6. Eliminar")
        print("0. Volver")
        op = input("Opción: ").strip()
        try:
            if op == "1":
                emp = crear_empleado_desde_entrada()
                EmpleadoDAO.insertar(emp)
                print(f"Empleado registrado con ID {emp.id}.")
            elif op == "2":
                empleados = EmpleadoDAO.listar()
                if not empleados:
                    print("No hay empleados registrados.")
                for emp in empleados:
                    print(emp)
            elif op == "3":
                emp = EmpleadoDAO.buscar_por_id(pedir_entero("ID: "))
                print(emp if emp else "Empleado no encontrado.")
            elif op == "4":
                emp = EmpleadoDAO.buscar_por_correo(input("Correo: "))
                print(emp if emp else "Empleado no encontrado.")
            elif op == "5":
                emp = EmpleadoDAO.buscar_por_id(pedir_entero("ID: "))
                if emp is None:
                    print("Empleado no encontrado.")
                    continue
                correo = input(f"Nuevo correo [{emp.correo}]: ").strip()
                if correo:
                    emp.cambiar_correo(correo)
                dep = pedir_entero("Nuevo ID departamento (Enter = mantener): ", permitir_vacio=True)
                if dep is not None:
                    emp.departamento_id = dep
                print("Actualizado." if EmpleadoDAO.actualizar(emp) else "Sin cambios.")
            elif op == "6":
                print("Eliminado." if EmpleadoDAO.eliminar(pedir_entero("ID: ")) else "Empleado no encontrado.")
            elif op == "0":
                return
            else:
                print("Opción no válida.")
        except ValueError as exc:
            print(f"Validación: {exc}")
        except Exception:
            print("No fue posible completar la operación de empleado.")


def menu_proyectos():
    while True:
        print("\n--- PROYECTOS ---")
        print("1. Crear")
        print("2. Listar")
        print("3. Actualizar")
        print("4. Eliminar")
        print("5. Asignar empleado")
        print("6. Ver empleados asignados")
        print("0. Volver")
        op = input("Opción: ").strip()
        try:
            if op == "1":
                p = Proyecto(nombre=input("Nombre: "), descripcion=input("Descripción: "))
                ProyectoDAO.insertar(p)
                print(f"Proyecto creado con ID {p.id}.")
            elif op == "2":
                items = ProyectoDAO.listar()
                if not items:
                    print("No hay proyectos.")
                for item in items:
                    print(item)
            elif op == "3":
                p = ProyectoDAO.buscar_por_id(pedir_entero("ID: "))
                if not p:
                    print("Proyecto no encontrado.")
                    continue
                p.nombre = input(f"Nombre [{p.nombre}]: ").strip() or p.nombre
                p.descripcion = input(f"Descripción [{p.descripcion}]: ").strip() or p.descripcion
                print("Actualizado." if ProyectoDAO.actualizar(p) else "Sin cambios.")
            elif op == "4":
                print("Eliminado." if ProyectoDAO.eliminar(pedir_entero("ID: ")) else "No encontrado.")
            elif op == "5":
                ProyectoDAO.asignar_empleado(pedir_entero("ID proyecto: "), pedir_entero("ID empleado: "))
                print("Empleado asignado al proyecto.")
            elif op == "6":
                items = ProyectoDAO.listar_empleados(pedir_entero("ID proyecto: "))
                if not items:
                    print("No hay empleados asignados.")
                for item in items:
                    print(item)
            elif op == "0":
                return
            else:
                print("Opción no válida.")
        except ValueError as exc:
            print(f"Validación: {exc}")
        except Exception:
            print("No fue posible completar la operación de proyecto. Verifica IDs duplicados o inexistentes.")


def menu_registros():
    while True:
        print("\n--- REGISTROS DE TIEMPO ---")
        print("1. Registrar horas")
        print("2. Listar")
        print("3. Actualizar")
        print("4. Eliminar")
        print("5. Total horas por proyecto")
        print("0. Volver")
        op = input("Opción: ").strip()
        try:
            if op == "1":
                r = RegistroTiempo(
                    empleado_id=pedir_entero("ID empleado: "),
                    proyecto_id=pedir_entero("ID proyecto: "),
                    horas=pedir_float("Horas: ", minimo=0.01),
                    descripcion=input("Descripción tarea: "),
                )
                RegistroTiempoDAO.insertar(r)
                print(f"Registro creado con ID {r.id}.")
            elif op == "2":
                items = RegistroTiempoDAO.listar()
                if not items:
                    print("No hay registros.")
                for item in items:
                    print(item)
            elif op == "3":
                r = RegistroTiempoDAO.buscar_por_id(pedir_entero("ID registro: "))
                if not r:
                    print("Registro no encontrado.")
                    continue
                horas = pedir_float(f"Nuevas horas [{r.horas}] (Enter = mantener): ", minimo=0.01, permitir_vacio=True)
                if horas is not None:
                    r.horas = horas
                desc = input(f"Descripción [{r.descripcion}]: ").strip()
                if desc:
                    r.descripcion = desc
                print("Actualizado." if RegistroTiempoDAO.actualizar(r) else "Sin cambios.")
            elif op == "4":
                print("Eliminado." if RegistroTiempoDAO.eliminar(pedir_entero("ID: ")) else "No encontrado.")
            elif op == "5":
                id_p = pedir_entero("ID proyecto: ")
                print(f"Total de horas: {RegistroTiempoDAO.horas_por_proyecto(id_p):.2f}")
            elif op == "0":
                return
            else:
                print("Opción no válida.")
        except ValueError as exc:
            print(f"Validación: {exc}")
        except Exception:
            print("No fue posible completar la operación de registro. Verifica que empleado y proyecto existan.")


def main():
    try:
        crear_tablas()
    except Exception:
        print("No fue posible preparar la base de datos. Revisa la configuración de .env.")
        return

    while True:
        print("\n========== ECOTECH ==========")
        print("1. Empleados")
        print("2. Departamentos")
        print("3. Proyectos")
        print("4. Registros de tiempo")
        print("0. Salir")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            menu_empleados()
        elif opcion == "2":
            menu_departamentos()
        elif opcion == "3":
            menu_proyectos()
        elif opcion == "4":
            menu_registros()
        elif opcion == "0":
            print("Hasta luego.")
            break
        else:
            print("Opción no válida.")


<<<<<<< HEAD

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

=======
if __name__ == "__main__":
    main()
>>>>>>> ac8be7d (Implementa avances Ev2: nuevas entidades, DAO, CRUD y documentacion)
