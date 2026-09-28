class Empleado:
    def __init__(self, nombre, correo, id=None):
        self.id = id
        self.nombre = nombre
        self.correo = correo

    def __str__(self):
        return f"Empleado(id={self.id}, nombre='{self.nombre}', correo='{self.correo}')"