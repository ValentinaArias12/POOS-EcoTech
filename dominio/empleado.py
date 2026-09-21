from dataclasses import dataclass


class Empleado:
    def __init__(self, nombre: str, correo: str):
        self.nombre = nombre
        self.correo = correo
        self._registros: list = [] 
