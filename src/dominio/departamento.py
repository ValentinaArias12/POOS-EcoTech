from dominio.empleado import Empleado

class Departamento:
    def __init__(self, nombre: str, id: int = None):
        self.id = id
        self.nombre = nombre
        self._empleados: list[Empleado] = []

    def agregar_empleado(self, empleado: Empleado):
        if empleado in self._empleados:
            return False
        self._empleados.append(empleado)
        return True

    def mostrar_datos(self) -> str:
        return f"[{self.id}] {self.nombre}"