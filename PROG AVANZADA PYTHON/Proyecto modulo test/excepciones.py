# =============================================================================
# excepciones.py — Jerarquía de excepciones personalizadas del GIC
# =============================================================================

class GICError(Exception):
    """Excepción base del sistema GIC. Todas las excepciones del sistema
    heredan de esta clase para facilitar el manejo en bloque."""
    def __init__(self, mensaje="Error en el sistema GIC"):
        super().__init__(mensaje)
        self.mensaje = mensaje

    def __str__(self):
        return f"[GICError] {self.mensaje}"


# ── Errores de validación ──────────────────────────────────────────────────

class ValidacionError(GICError):
    """Excepción base para errores de validación de datos."""
    def __init__(self, campo, valor, razon):
        self.campo = campo
        self.valor = valor
        self.razon = razon
        super().__init__(f"Validación fallida en '{campo}': {razon} (valor recibido: '{valor}')")

    def __str__(self):
        return f"[ValidacionError] Campo '{self.campo}' → {self.razon}"


class EmailInvalidoError(ValidacionError):
    """Se lanza cuando el formato del email no es válido."""
    def __init__(self, email):
        super().__init__("email", email, "debe contener '@' y un dominio válido")

    def __str__(self):
        return f"[EmailInvalidoError] '{self.valor}' no es un email válido"


class TelefonoInvalidoError(ValidacionError):
    """Se lanza cuando el teléfono no cumple el formato esperado."""
    def __init__(self, telefono):
        super().__init__("telefono", telefono, "debe contener solo dígitos y tener entre 7 y 15 caracteres")

    def __str__(self):
        return f"[TelefonoInvalidoError] '{self.valor}' no es un teléfono válido"


class DireccionInvalidaError(ValidacionError):
    """Se lanza cuando la dirección está vacía o es demasiado corta."""
    def __init__(self, direccion):
        super().__init__("direccion", direccion, "debe tener al menos 5 caracteres")

    def __str__(self):
        return f"[DireccionInvalidaError] '{self.valor}' no es una dirección válida"


class NombreInvalidoError(ValidacionError):
    """Se lanza cuando el nombre no cumple los requisitos mínimos."""
    def __init__(self, nombre):
        super().__init__("nombre", nombre, "debe tener al menos 2 caracteres y no contener números")

    def __str__(self):
        return f"[NombreInvalidoError] '{self.valor}' no es un nombre válido"


class TipoInvalidoError(ValidacionError):
    """Se lanza cuando un valor no es del tipo Python esperado (isinstance)."""
    def __init__(self, campo, tipo_esperado, tipo_recibido):
        self.tipo_esperado = tipo_esperado
        self.tipo_recibido = tipo_recibido
        super().__init__(
            campo,
            str(tipo_recibido),
            f"se esperaba {tipo_esperado.__name__}, se recibió {tipo_recibido.__name__}"
        )

    def __str__(self):
        return (f"[TipoInvalidoError] Campo '{self.campo}': "
                f"esperado {self.tipo_esperado.__name__}, "
                f"recibido {self.tipo_recibido.__name__}")


# ── Errores de cliente ─────────────────────────────────────────────────────

class ClienteError(GICError):
    """Excepción base para errores relacionados con clientes."""
    pass


class ClienteNoEncontradoError(ClienteError):
    """Se lanza cuando no se encuentra un cliente por su ID."""
    def __init__(self, cliente_id):
        self.cliente_id = cliente_id
        super().__init__(f"No se encontró ningún cliente con ID {cliente_id}")

    def __str__(self):
        return f"[ClienteNoEncontradoError] ID {self.cliente_id} no existe en el sistema"


class ClienteDuplicadoError(ClienteError):
    """Se lanza cuando se intenta agregar un cliente con ID o email ya existente."""
    def __init__(self, campo, valor):
        self.campo = campo
        self.valor = valor
        super().__init__(f"Ya existe un cliente con {campo} = '{valor}'")

    def __str__(self):
        return f"[ClienteDuplicadoError] {self.campo} '{self.valor}' ya está registrado"


# ── Errores de persistencia ────────────────────────────────────────────────

class PersistenciaError(GICError):
    """Excepción base para errores de lectura/escritura de datos."""
    pass


class ArchivoError(PersistenciaError):
    """Se lanza ante fallos al leer o escribir archivos JSON/CSV."""
    def __init__(self, ruta, operacion, detalle=""):
        self.ruta = ruta
        self.operacion = operacion
        mensaje = f"Error al {operacion} el archivo '{ruta}'"
        if detalle:
            mensaje += f": {detalle}"
        super().__init__(mensaje)

    def __str__(self):
        return f"[ArchivoError] {self.mensaje}"


class BaseDatosError(PersistenciaError):
    """Se lanza ante errores en la conexión o consultas SQLite."""
    def __init__(self, operacion, detalle=""):
        self.operacion = operacion
        mensaje = f"Error en base de datos durante '{operacion}'"
        if detalle:
            mensaje += f": {detalle}"
        super().__init__(mensaje)

    def __str__(self):
        return f"[BaseDatosError] {self.mensaje}"