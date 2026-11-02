import math
import requests

def obtener_datos_api() -> dict:
    """Realiza la solicitud HTTP GET a la API de tipos de cambio (USD)."""
    url = "https://open.er-api.com/v6/latest/USD"
    respuesta = requests.get(url, timeout=(3, 5))
    respuesta.raise_for_status()  # Lanza excepción si el estado HTTP no es 200 OK
    return respuesta.json()

def extraer_tasa_clp(datos: dict) -> tuple[str, float]:
    """Valida la estructura de la respuesta y extrae la fecha y la tasa del peso chileno (CLP)."""
    if not isinstance(datos, dict):
        raise ValueError("La respuesta recibida no es un diccionario válido.")
    
    # 1. Verificar que el resultado indicado por la API sea exitoso
    if datos.get("result") != "success":
        raise ValueError("La API devolvió un estado de respuesta no exitoso.")
    
    # 2. Extraer el diccionario de tasas de cambio
    rates = datos.get("rates")
    if not isinstance(rates, dict):
        raise ValueError("El campo 'rates' no está presente o no es un diccionario.")
    
    valor_clp = rates.get("CLP")
    fecha_utc = datos.get("time_last_update_utc", "Fecha no disponible")
    
    # 3. Validar que la tasa sea un número positivo y finito
    if (
        type(valor_clp) not in (int, float)
        or not math.isfinite(valor_clp)
        or valor_clp <= 0
    ):
        raise ValueError("La tasa de cambio para CLP es inválida o negativa.")
        
    return str(fecha_utc), float(valor_clp)

def consultar_dolar_observado():
    print("\n==========================================")
    print(" CONSULTA TASA DE CAMBIO (USD / CLP)")
    print("==========================================")
    try:
        datos = obtener_datos_api()
        fecha, valor = extraer_tasa_clp(datos)
        
        fecha_corta = fecha[:16] if len(fecha) >= 16 else fecha
        
        print(f" Tasa de cambio: ${valor:.2f} CLP por 1 USD")
        print(f" Última actualización: {fecha_corta}")
        print(" Fuente: open.er-api.com")
        
    except requests.exceptions.RequestException:
        print(" No fue posible conectar con el servicio de tipo de cambio. Reintente más tarde.")
    except (ValueError, KeyError, TypeError) as err:
        print(f" Respuesta de API no válida: {err}")