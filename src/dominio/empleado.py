from datetime import date

class Empleado:
    """Clase base del dominio EcoTech. No conoce SQL ni detalles de persistencia."""
    TIPO = "BASE"
    MIN_NOMBRE = 2
    MAX_NOMBRE = 120
    MIN_CORREO = 6
    MAX_CORREO = 150
    MAX_TELEFONO = 30

    def __init__(
        self,
        nombre: str,
        correo: str,
        telefono: str = "",
        fecha_inicio: str | None = None,
        salario_base: float = 0.0,
        tipo: str = "BASE",
        bono_anual: float = 0.0,
        tarifa_hora: float = 0.0,
        departamento_id: int | None = None,
        id: int | None = None,
    ):
        self.id = id
        self.nombre = self._validar_nombre(nombre)
        self._correo = self._validar_correo(correo)
        self.telefono = self._validar_telefono(telefono)
        self.fecha_inicio = fecha_inicio or date.today().isoformat()
        self.salario_base = self._validar_salario(salario_base)
        self.tipo = tipo or self.TIPO
        self.bono_anual = self._validar_salario(bono_anual)
        self.tarifa_hora = self._validar_salario(tarifa_hora)
        self.departamento_id = departamento_id

    @classmethod
    def _validar_nombre(cls, nombre: str) -> str:
        """Valida que el nombre sea texto y cumpla los límites de longitud."""
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser texto.")
        nombre = nombre.strip()
        if not cls.MIN_NOMBRE <= len(nombre) <= cls.MAX_NOMBRE:
            raise ValueError(
                f"El nombre debe tener entre {cls.MIN_NOMBRE} y {cls.MAX_NOMBRE} caracteres."
            )
        return nombre

    @classmethod
    def _validar_correo(cls, correo: str) -> str:
        """Valida longitud y formato del correo electrónico."""
        if not isinstance(correo, str):
            raise TypeError("El correo debe ser texto.")
        correo = correo.strip().lower()
        if not cls.MIN_CORREO <= len(correo) <= cls.MAX_CORREO:
            raise ValueError(
                f"El correo debe tener entre {cls.MIN_CORREO} y {cls.MAX_CORREO} caracteres."
            )
        if "@" not in correo or "." not in correo.split("@")[-1]:
            raise ValueError("El correo debe tener un formato válido (ejemplo: usuario@dominio.com).")
        return correo

    @classmethod
    def _validar_telefono(cls, telefono: str) -> str:
        """Valida que el teléfono no exceda el largo máximo permitido."""
        telefono = (telefono or "").strip()
        if len(telefono) > cls.MAX_TELEFONO:
            raise ValueError(f"El teléfono no puede superar los {cls.MAX_TELEFONO} caracteres.")
        return telefono

    @staticmethod
    def _validar_salario(valor: float) -> float:
        try:
            valor = float(valor)
        except (TypeError, ValueError) as exc:
            raise ValueError("El salario/monto debe ser numérico.") from exc
        if valor < 0:
            raise ValueError("El monto no puede ser negativo.")
        return valor

    @property
    def correo(self) -> str:
        return self._correo

    def cambiar_correo(self, nuevo_correo: str) -> None:
        self._correo = self._validar_correo(nuevo_correo)

    def calcular_salario(self) -> float:
        return self.salario_base

    def obtener_detalles(self) -> str:
        depto_str = f"ID {self.departamento_id}" if self.departamento_id else "Sin asignar"
        return (
            f"[{self.id or 'Nuevo'}] {self.nombre} | Correo: {self.correo} | "
            f"Tipo: {self.tipo} | Depto: {depto_str}"
        )

    def __str__(self) -> str:
        return self.obtener_detalles()


class EmpleadoPlanta(Empleado):
    TIPO = "PLANTA"

    def __init__(self, *args, bono_anual: float = 0.0, **kwargs):
        kwargs["tipo"] = "PLANTA"
        kwargs["bono_anual"] = bono_anual
        super().__init__(*args, **kwargs)

    def calcular_salario(self) -> float:
        return self.salario_base + (self.bono_anual / 12)


class EmpleadoContrata(Empleado):
    TIPO = "CONTRATA"

    def __init__(self, *args, tarifa_hora: float = 0.0, **kwargs):
        kwargs["tipo"] = "CONTRATA"
        kwargs["tarifa_hora"] = tarifa_hora
        super().__init__(*args, **kwargs)

    def calcular_salario(self) -> float:
        return self.salario_base