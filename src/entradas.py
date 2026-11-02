
def pedir_dato(mensaje: str, validador):
    """
    Solicita un dato al usuario y lo valida usando la función validador proporcionada.
    Si la validación falla, muestra el error y vuelve a pedir
    ÚNICAMENTE este campo sin cancelar el formulario.
    """
    while True:
        try:
            entrada = input(mensaje)
            return validador(entrada)
        except (TypeError, ValueError) as error:
            print(f" {error} Intente nuevamente.\n")