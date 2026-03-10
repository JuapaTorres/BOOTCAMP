# =============================================================================
# cliente.py — Clase base Cliente con encapsulación completa
# =============================================================================
from validaciones import validar_nombre, validar_email, validar_telefono, validar_direccion
from excepciones import ValidacionError


class Cliente:
    """Clase base que representa un cliente del sistema GIC.
    
    Aplica encapsulación con atributos privados y validaciones en cada setter.
    Sirve como clase base para ClienteRegular, ClientePremium y ClienteCorporativo.
    
    Attributes (privados):
        __id (int): Identificador único del cliente.
        __nombre (str): Nombre completo.
        __email (str): Correo electrónico validado.
        __telefono (str): Teléfono de contacto (opcional).
        __direccion (str): Dirección física (opcional).
    """

    def __init__(self, cliente_id, nombre, email, telefono="", direccion=""):
        """Inicializa un cliente con validaciones en cada campo.
        
        Args:
            cliente_id (int): ID único del cliente.
            nombre (str): Nombre completo.
            email (str): Email válido.
            telefono (str, opcional): Teléfono de contacto.
            direccion (str, opcional): Dirección física.
        
        Raises:
            TipoInvalidoError: Si algún campo no es del tipo correcto.
            NombreInvalidoError, EmailInvalidoError, etc.: Según validación.
        """
        self.__id = cliente_id
        self.set_nombre(nombre)
        self.set_email(email)
        # Campos opcionales: solo validar si se proporcionan
        self.__telefono = validar_telefono(telefono) if telefono else ""
        self.__direccion = validar_direccion(direccion) if direccion else ""

    # ── Getters ───────────────────────────────────────────────────────────

    def get_id(self):
        """Retorna el ID único del cliente."""
        return self.__id

    def get_nombre(self):
        """Retorna el nombre del cliente."""
        return self.__nombre

    def get_email(self):
        """Retorna el email del cliente."""
        return self.__email

    def get_telefono(self):
        """Retorna el teléfono del cliente."""
        return self.__telefono

    def get_direccion(self):
        """Retorna la dirección del cliente."""
        return self.__direccion

    def get_tipo(self):
        """Retorna el tipo de cliente como string. Sobrescrito en subclases."""
        return "Base"

    # ── Setters con validación ─────────────────────────────────────────────

    def set_nombre(self, nombre):
        """Setter con validación para el nombre.
        
        Raises:
            NombreInvalidoError: Si el nombre no es válido.
        """
        self.__nombre = validar_nombre(nombre)

    def set_email(self, email):
        """Setter con validación para el email.
        
        Raises:
            EmailInvalidoError: Si el email no tiene formato correcto.
        """
        self.__email = validar_email(email)

    def set_telefono(self, telefono):
        """Setter con validación para el teléfono.
        
        Raises:
            TelefonoInvalidoError: Si el teléfono no es válido.
        """
        self.__telefono = validar_telefono(telefono) if telefono else ""

    def set_direccion(self, direccion):
        """Setter con validación para la dirección.
        
        Raises:
            DireccionInvalidaError: Si la dirección es demasiado corta.
        """
        self.__direccion = validar_direccion(direccion) if direccion else ""

    # ── Método polimórfico ─────────────────────────────────────────────────

    def calcular_descuento(self):
        """Calcula el descuento aplicable al cliente.
        Método polimórfico: cada subclase implementa su propia lógica.
        
        Returns:
            float: Porcentaje de descuento (0 por defecto en la clase base).
        """
        return 0

    def info_extra(self):
        """Retorna información adicional específica del tipo de cliente.
        Método polimórfico sobrescrito en subclases.
        
        Returns:
            str: Información extra del cliente.
        """
        return "Sin información adicional"

    # ── Serialización ──────────────────────────────────────────────────────

    def to_dict(self):
        """Serializa el cliente a un diccionario para JSON/CSV.
        
        Returns:
            dict: Representación del cliente como diccionario.
        """
        return {
            "id": self.__id,
            "tipo": self.get_tipo(),
            "nombre": self.__nombre,
            "email": self.__email,
            "telefono": self.__telefono,
            "direccion": self.__direccion,
            "descuento": self.calcular_descuento()
        }

    # ── Métodos especiales ─────────────────────────────────────────────────

    def __str__(self):
        """Representación legible del cliente."""
        return (
            f"[{self.get_tipo()}] ID: {self.__id} | "
            f"Nombre: {self.__nombre} | "
            f"Email: {self.__email} | "
            f"Descuento: {self.calcular_descuento()}%"
        )

    def __repr__(self):
        """Representación técnica del cliente."""
        return (
            f"{self.__class__.__name__}("
            f"id={self.__id!r}, "
            f"nombre={self.__nombre!r}, "
            f"email={self.__email!r})"
        )

    def __eq__(self, other):
        """Dos clientes son iguales si tienen el mismo ID o el mismo email."""
        if not isinstance(other, Cliente):
            return NotImplemented
        return self.__id == other.__id or self.__email == other.__email