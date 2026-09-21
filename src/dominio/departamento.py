class Departamento:
    def __init__(self, nombre: str, id: int = None):
        self.id = id
        self.nombre = nombre

    def mostrar_datos(self) -> str:
        return f"[{self.id}] {self.nombre}"