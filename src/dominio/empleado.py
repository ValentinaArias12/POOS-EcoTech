from datetime import date

<<<<<<< HEAD
    def mostrar_datos(self) -> str:
        return f"[{self.id}] {self.nombre} - {self.correo}"

    def __str__(self) -> str:
        return self.mostrar_datos()

=======

class Empleado:
    """Clase base del dominio. No conoce SQL ni detalles de persistencia."""

    TIPO = "BASE"

    def __init__(
        self,
        nombre: str,
        correo: str,
        telefono: str = "",
        fecha_inicio: str | None = None,
        salario_base: float = 0.0,
        departamento_id: int | None = None,
        id: int | None = None,
    ):
        self.id = id
        self.nombre = self._validar_nombre(nombre)
        self._correo = self._validar_correo(correo)
        self.telefono = telefono.strip()
        self.fecha_inicio = fecha_inicio or date.today().isoformat()
        self.salario_base = self._validar_salario(salario_base)
        self.departamento_id = departamento_id

    @staticmethod
    def _validar_nombre(nombre: str) -> str:
        nombre = nombre.strip()
        if len(nombre) < 2:
            raise ValueError("El nombre debe tener al menos 2 caracteres.")
        return nombre

    @staticmethod
    def _validar_correo(correo: str) -> str:
        correo = correo.strip().lower()
        if "@" not in correo or "." not in correo.split("@")[-1]:
            raise ValueError("El correo no tiene un formato válido.")
        return correo

    @staticmethod
    def _validar_salario(valor: float) -> float:
        try:
            valor = float(valor)
        except (TypeError, ValueError) as exc:
            raise ValueError("El salario debe ser numérico.") from exc
        if valor < 0:
            raise ValueError("El salario no puede ser negativo.")
        return valor

    @property
    def correo(self) -> str:
        return self._correo

    def cambiar_correo(self, nuevo_correo: str) -> None:
        self._correo = self._validar_correo(nuevo_correo)

    def calcular_salario(self) -> float:
        return self.salario_base

    def obtener_detalles(self) -> str:
        return (
            f"[{self.id}] {self.nombre} | {self.correo} | "
            f"Tipo: {self.TIPO} | Depto: {self.departamento_id or 'Sin asignar'}"
        )

    def __str__(self) -> str:
        return self.obtener_detalles()


class EmpleadoPlanta(Empleado):
    TIPO = "PLANTA"

    def __init__(self, *args, bono_anual: float = 0.0, **kwargs):
        super().__init__(*args, **kwargs)
        self.bono_anual = self._validar_salario(bono_anual)

    def calcular_salario(self) -> float:
        # Regla demostrativa del proyecto: salario mensual + prorrateo del bono anual.
        return self.salario_base + (self.bono_anual / 12)


class EmpleadoContrata(Empleado):
    TIPO = "CONTRATA"

    def __init__(self, *args, tarifa_hora: float = 0.0, **kwargs):
        super().__init__(*args, **kwargs)
        self.tarifa_hora = self._validar_salario(tarifa_hora)

    def calcular_salario(self) -> float:
        # Para no inventar horas trabajadas, el cálculo base conserva salario_base.
        return self.salario_base
>>>>>>> ac8be7d (Implementa avances Ev2: nuevas entidades, DAO, CRUD y documentacion)
