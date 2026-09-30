class Empleado:
    def __init__(self, nombre, correo, id=None):
        self.id = id
        self.nombre = nombre
        self.correo = correo

    def mostrar_datos(self) -> str:
        return f"[{self.id}] {self.nombre} - {self.correo}"

    def __str__(self) -> str:
        return self.mostrar_datos()

