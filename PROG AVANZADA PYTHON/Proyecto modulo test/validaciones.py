# =============================================================================
# validaciones.py — Validaciones centralizadas con isinstance y raise
# =============================================================================
import re
from excepciones import (
    EmailInvalidoError, TelefonoInvalidoError, DireccionInvalidaError,
    NombreInvalidoError, TipoInvalidoError
)


def validar_tipo(valor, tipo_esperado, campo):
    """Valida que un valor sea del tipo correcto usando isinstance().
    Lanza TipoInvalidoError si no coincide.
    
    Args:
        valor: El valor a validar.
        tipo_esperado (type): El tipo Python esperado (str, int, float, etc.).
        campo (str): Nombre del campo para el mensaje de error.
    
    Raises:
        TipoInvalidoError: Si el valor no es del tipo esperado.
    """
    if not isinstance(valor, tipo_esperado):
        raise TipoInvalidoError(campo, tipo_esperado, type(valor))


def validar_nombre(nombre):
    """Valida que el nombre sea un string con al menos 2 caracteres sin dígitos.
    
    Args:
        nombre (str): Nombre a validar.
    
    Returns:
        str: Nombre limpio (strip).
    
    Raises:
        TipoInvalidoError: Si no es string.
        NombreInvalidoError: Si no cumple el formato.
    """
    validar_tipo(nombre, str, "nombre")
    nombre = nombre.strip()
    if len(nombre) < 2 or any(c.isdigit() for c in nombre):
        raise NombreInvalidoError(nombre)
    return nombre


def validar_email(email):
    """Valida que el email tenga formato usuario@dominio.ext.
    
    Args:
        email (str): Email a validar.
    
    Returns:
        str: Email en minúsculas y sin espacios.
    
    Raises:
        TipoInvalidoError: Si no es string.
        EmailInvalidoError: Si el formato no es válido.
    """
    validar_tipo(email, str, "email")
    email = email.strip().lower()
    patron = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    if not re.match(patron, email):
        raise EmailInvalidoError(email)
    return email


def validar_telefono(telefono):
    """Valida que el teléfono contenga solo dígitos (y opcionalmente '+') 
    con longitud entre 7 y 15 caracteres.
    
    Args:
        telefono (str): Teléfono a validar.
    
    Returns:
        str: Teléfono limpio.
    
    Raises:
        TipoInvalidoError: Si no es string.
        TelefonoInvalidoError: Si el formato no es válido.
    """
    validar_tipo(telefono, str, "telefono")
    telefono = telefono.strip().replace(" ", "").replace("-", "")
    patron = r'^\+?\d{7,15}$'
    if not re.match(patron, telefono):
        raise TelefonoInvalidoError(telefono)
    return telefono


def validar_direccion(direccion):
    """Valida que la dirección tenga al menos 5 caracteres.
    
    Args:
        direccion (str): Dirección a validar.
    
    Returns:
        str: Dirección limpia.
    
    Raises:
        TipoInvalidoError: Si no es string.
        DireccionInvalidaError: Si es demasiado corta.
    """
    validar_tipo(direccion, str, "direccion")
    direccion = direccion.strip()
    if len(direccion) < 5:
        raise DireccionInvalidaError(direccion)
    return direccion


def validar_puntos(puntos):
    """Valida que los puntos sean un entero no negativo.
    
    Args:
        puntos (int): Puntos a validar.
    
    Returns:
        int: Puntos validados.
    
    Raises:
        TipoInvalidoError: Si no es entero.
        ValueError: Si es negativo.
    """
    validar_tipo(puntos, int, "puntos")
    if puntos < 0:
        raise ValueError(f"Los puntos no pueden ser negativos, se recibió: {puntos}")
    return puntos


def validar_empresa(empresa):
    """Valida que el nombre de empresa sea un string con al menos 2 caracteres.
    
    Args:
        empresa (str): Nombre de empresa a validar.
    
    Returns:
        str: Empresa limpia.
    
    Raises:
        TipoInvalidoError: Si no es string.
        ValueError: Si está vacía.
    """
    validar_tipo(empresa, str, "empresa")
    empresa = empresa.strip()
    if len(empresa) < 2:
        raise ValueError(f"El nombre de empresa debe tener al menos 2 caracteres: '{empresa}'")
    return empresa