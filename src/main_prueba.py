# En un archivo Python de prueba:
import requests

def obtener_datos():
    respuesta = requests.get(
        "https://open.er-api.com/v6/latest/USD",
        timeout=(3, 5),
    )
    respuesta.raise_for_status()
    return respuesta.json()


def extraer_datos():
    datos = obtener_datos()
    return {
        "unidad": datos["rates"],
        "fecha": datos["date"],
        "origen": datos["base"],
    }
