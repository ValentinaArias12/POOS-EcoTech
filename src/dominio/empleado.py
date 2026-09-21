class Empleado:
    def __init__(self, nombre: str, correo: str, id: int = None):
        self.id = id
        self.nombre = nombre
        self.correo = correo

    def mostrar_datos(self) -> str:
        return f"[{self.id}] {self.nombre} - {self.correo}"