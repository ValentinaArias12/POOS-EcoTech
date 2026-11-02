import bcrypt
from dominio.usuario import Usuario
from persistencia.empleado_dao import EmpleadoDAO
from persistencia.usuario_dao import UsuarioDAO


MAX_BYTES_BCRYPT = 72

def crear_hash(clave: str) -> str:
    """Valida la clave usando la regla del dominio y genera el hash seguro con bcrypt."""
    clave = Usuario.validar_clave(clave)
    clave_bytes = clave.encode("utf-8")
    if len(clave_bytes) > MAX_BYTES_BCRYPT:
        raise ValueError("La contraseña no puede superar los 72 bytes.")

    return bcrypt.hashpw(clave_bytes, bcrypt.gensalt()).decode("utf-8")

def registrar_usuario(
    empleado_id: int,
    nombre_usuario: str,
    clave: str,
    rol: str = "empleado"
) -> int:
    """Registra una nueva cuenta vinculada a un empleado existente."""
    # 1. Verificar que el empleado exista en la BD
    empleado = EmpleadoDAO.buscar_por_id(empleado_id)
    if empleado is None:
        raise ValueError("El empleado ingresado no existe.")
    
    # 2. Verificar que el empleado no tenga ya una cuenta registrada
    if UsuarioDAO.buscar_por_empleado(empleado_id) is not None:
        raise ValueError("El empleado ya tiene una cuenta de usuario asociada.")
    
    # 3. Normalizar usuario y verificar duplicados de nombre de acceso
    nombre_normalizado = Usuario.normalizar_usuario(nombre_usuario)
    if UsuarioDAO.buscar_por_nombre(nombre_normalizado) is not None:
        raise ValueError("El nombre de usuario ya se encuentra registrado.")
    
    # 4. Generar hash y construir el objeto Usuario con su rol
    hash_guardado = crear_hash(clave)
    usuario = Usuario(
        nombre_usuario=nombre_normalizado,
        password_hash=hash_guardado,
        empleado_id=empleado_id,
        rol=rol,
    )
    
    # 5. Guardar mediante el DAO y retornar el ID generado
    return UsuarioDAO.insertar(usuario)

def autenticar(nombre_usuario: str, clave: str) -> dict | None:
    """Verifica las credenciales y devuelve la sesión si es válida, o None si falla."""
    if not isinstance(clave, str):
        return None
    clave_bytes = clave.encode("utf-8")
    if not 0 < len(clave_bytes) <= MAX_BYTES_BCRYPT:
        return None

    # Normalizar para buscar exactamente el usuario guardado
    try:
        nombre_normalizado = Usuario.normalizar_usuario(nombre_usuario)
    except (TypeError, ValueError):
        return None

    cuenta = UsuarioDAO.buscar_por_nombre(nombre_normalizado)
    if cuenta is None:
        return None

    # Comprobar la contraseña usando bcrypt.checkpw
    if not bcrypt.checkpw(clave_bytes, cuenta.password_hash.encode("utf-8")):
        return None

    # Retornar los datos esenciales de la sesión iniciada
    return {
        "id": cuenta.id,
        "empleado_id": cuenta.empleado_id,
        "nombre_usuario": cuenta.nombre_usuario,
        "rol": cuenta.rol,
    }