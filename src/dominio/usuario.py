

class Usuario:
    MIN_USUARIO = 3
    MAX_USUARIO = 40
    MIN_CLAVE = 6

    def __init__(self, nombre_usuario: str, password_hash: str, empleado_id: int, id: int | None = None):
        if not isinstance(empleado_id, int) or empleado_id <= 0:
            raise ValueError("El ID del empleado debe ser un entero positivo.")
        self.id = id
        self.empleado_id = empleado_id
        self.nombre_usuario = self.normalizar_usuario(nombre_usuario)
        self.password_hash = password_hash

    @classmethod
    def normalizar_usuario(cls, nombre: str) -> str:
        """Sanea y normaliza el nombre de usuario (espacios, minúsculas y caracteres)."""
        if not isinstance(nombre, str):
            raise TypeError("El usuario debe ser texto.")
        nombre = nombre.strip().lower()
        if not cls.MIN_USUARIO <= len(nombre) <= cls.MAX_USUARIO:
            raise ValueError(f"El usuario debe tener entre {cls.MIN_USUARIO} y {cls.MAX_USUARIO} caracteres.")
        if not all(c.isascii() and (c.isalnum() or c == "_") for c in nombre):
            raise ValueError("El usuario solo permite letras ASCII, números y guion bajo (_).")
        return nombre

    @classmethod
    def validar_clave(cls, clave: str) -> str:
        """Valida que la clave cumpla el largo mínimo (conserva mayúsculas y espacios internos)."""
        if not isinstance(clave, str):
            raise TypeError("La contraseña debe ser texto.")
        if len(clave) < cls.MIN_CLAVE:
            raise ValueError(f"La contraseña debe tener al menos {cls.MIN_CLAVE} caracteres.")
        return clave