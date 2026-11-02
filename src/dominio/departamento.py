from dominio.empleado import Empleado

class Departamento:
    """Entidad de dominio que representa un departamento de EcoTech."""

    MIN_NOMBRE_LENGTH = 2
    MAX_NOMBRE_LENGTH = 100
    
    def __init__(self, nombre: str, id: int | None = None):
        nombre = nombre.strip()
        if not nombre:
            raise ValueError("El nombre del departamento es obligatorio.")
        if len(nombre) < self.MIN_NOMBRE_LENGTH or len(nombre) > self.MAX_NOMBRE_LENGTH:
            raise ValueError(f"El nombre del departamento debe tener entre {self.MIN_NOMBRE_LENGTH} y {self.MAX_NOMBRE_LENGTH} caracteres.")
        self.id = id
        self.nombre = nombre
        self._empleados: list[Empleado] = []

    def agregar_empleado(self, empleado: Empleado):
        if empleado in self._empleados:
            return False
        self._empleados.append(empleado)
        return True

    def agregar_empleado(self, empleado) -> bool:
        if empleado in self._empleados:
            return False
        self._empleados.append(empleado)
        empleado.departamento_id = self.id
        return True

    @property
    def empleados(self) -> tuple:
        return tuple(self._empleados)

    def __str__(self) -> str:
        return f"Departamento(id={self.id}, nombre='{self.nombre}')"
