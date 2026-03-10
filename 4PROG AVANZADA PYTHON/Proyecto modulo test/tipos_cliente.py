# =============================================================================
# tipos_cliente.py — Subclases con herencia, polimorfismo y super()
# =============================================================================
from cliente import Cliente
from validaciones import validar_puntos, validar_empresa


class ClienteRegular(Cliente):
    """Cliente estándar con sistema de puntos para descuentos.
    
    El descuento se calcula como puntos * 0.01 (1 punto = 0.01% de descuento).
    Máximo descuento: 15%.
    
    Args:
        puntos (int): Puntos acumulados del cliente (default 0).
    """

    DESCUENTO_MAXIMO = 15.0

    def __init__(self, cliente_id, nombre, email, puntos=0, telefono="", direccion=""):
        """Inicializa un cliente regular.
        
        Args:
            cliente_id (int): ID único.
            nombre (str): Nombre completo.
            email (str): Email válido.
            puntos (int): Puntos acumulados (>= 0).
            telefono (str, opcional): Teléfono.
            direccion (str, opcional): Dirección.
        
        Raises:
            TipoInvalidoError: Si puntos no es entero.
            ValueError: Si puntos es negativo.
        """
        super().__init__(cliente_id, nombre, email, telefono, direccion)
        self.__puntos = validar_puntos(puntos)

    def get_puntos(self):
        """Retorna los puntos acumulados."""
        return self.__puntos

    def set_puntos(self, puntos):
        """Actualiza los puntos con validación.
        
        Raises:
            TipoInvalidoError: Si puntos no es entero.
            ValueError: Si es negativo.
        """
        self.__puntos = validar_puntos(puntos)

    def agregar_puntos(self, cantidad):
        """Suma puntos al acumulado actual.
        
        Args:
            cantidad (int): Puntos a agregar (debe ser positivo).
        
        Raises:
            ValueError: Si la cantidad es negativa.
        """
        validar_puntos(cantidad)
        self.__puntos += cantidad

    def calcular_descuento(self):
        """Descuento basado en puntos: 1 punto = 0.01%.
        Limitado al DESCUENTO_MAXIMO.
        
        Returns:
            float: Porcentaje de descuento entre 0 y 15.
        """
        descuento = self.__puntos * 0.01
        return min(descuento, self.DESCUENTO_MAXIMO)

    def get_tipo(self):
        return "Regular"

    def info_extra(self):
        return f"Puntos acumulados: {self.__puntos} | Descuento actual: {self.calcular_descuento():.2f}%"

    def to_dict(self):
        """Extiende el diccionario base con los puntos."""
        datos = super().to_dict()
        datos["puntos"] = self.__puntos
        return datos

    def __str__(self):
        return super().__str__() + f" | Puntos: {self.__puntos}"


class ClientePremium(Cliente):
    """Cliente premium con descuento fijo y beneficios adicionales.
    
    Siempre recibe un 20% de descuento más beneficios configurables.
    
    Args:
        beneficios (list[str]): Lista de beneficios especiales del cliente.
    """

    DESCUENTO_FIJO = 20.0

    def __init__(self, cliente_id, nombre, email, beneficios=None, telefono="", direccion=""):
        """Inicializa un cliente premium.
        
        Args:
            cliente_id (int): ID único.
            nombre (str): Nombre completo.
            email (str): Email válido.
            beneficios (list, opcional): Lista de beneficios extra.
            telefono (str, opcional): Teléfono.
            direccion (str, opcional): Dirección.
        """
        super().__init__(cliente_id, nombre, email, telefono, direccion)
        self.__beneficios = beneficios if isinstance(beneficios, list) else []

    def get_beneficios(self):
        """Retorna la lista de beneficios."""
        return self.__beneficios.copy()

    def agregar_beneficio(self, beneficio):
        """Agrega un beneficio a la lista.
        
        Args:
            beneficio (str): Beneficio a agregar.
        
        Raises:
            TypeError: Si el beneficio no es string.
        """
        if not isinstance(beneficio, str):
            raise TypeError(f"El beneficio debe ser un string, se recibió: {type(beneficio).__name__}")
        if beneficio.strip() and beneficio not in self.__beneficios:
            self.__beneficios.append(beneficio.strip())

    def calcular_descuento(self):
        """Descuento fijo del 20% para clientes premium.
        
        Returns:
            float: 20.0 siempre.
        """
        return self.DESCUENTO_FIJO

    def get_tipo(self):
        return "Premium"

    def info_extra(self):
        if self.__beneficios:
            return f"Beneficios: {', '.join(self.__beneficios)}"
        return "Sin beneficios adicionales configurados"

    def to_dict(self):
        """Extiende el diccionario base con los beneficios."""
        datos = super().to_dict()
        datos["beneficios"] = self.__beneficios
        return datos

    def __str__(self):
        return super().__str__() + f" | Beneficios: {len(self.__beneficios)}"


class ClienteCorporativo(Cliente):
    """Cliente corporativo asociado a una empresa con descuento máximo.
    
    Recibe un 30% de descuento y tiene un contacto principal en la empresa.
    
    Args:
        empresa (str): Nombre de la empresa.
        contacto (str): Nombre del contacto principal (opcional).
    """

    DESCUENTO_FIJO = 30.0

    def __init__(self, cliente_id, nombre, email, empresa, contacto="", telefono="", direccion=""):
        """Inicializa un cliente corporativo.
        
        Args:
            cliente_id (int): ID único.
            nombre (str): Nombre del representante.
            email (str): Email corporativo.
            empresa (str): Nombre de la empresa.
            contacto (str, opcional): Nombre del contacto principal.
            telefono (str, opcional): Teléfono.
            direccion (str, opcional): Dirección.
        
        Raises:
            TipoInvalidoError: Si empresa no es string.
            ValueError: Si empresa está vacía.
        """
        super().__init__(cliente_id, nombre, email, telefono, direccion)
        self.__empresa = validar_empresa(empresa)
        self.__contacto = contacto.strip() if isinstance(contacto, str) else ""

    def get_empresa(self):
        """Retorna el nombre de la empresa."""
        return self.__empresa

    def get_contacto(self):
        """Retorna el nombre del contacto principal."""
        return self.__contacto

    def set_empresa(self, empresa):
        """Actualiza el nombre de la empresa con validación.
        
        Raises:
            TipoInvalidoError / ValueError: Si la empresa no es válida.
        """
        self.__empresa = validar_empresa(empresa)

    def set_contacto(self, contacto):
        """Actualiza el contacto principal.
        
        Raises:
            TypeError: Si contacto no es string.
        """
        if not isinstance(contacto, str):
            raise TypeError("El contacto debe ser un string")
        self.__contacto = contacto.strip()

    def calcular_descuento(self):
        """Descuento fijo del 30% para clientes corporativos.
        
        Returns:
            float: 30.0 siempre.
        """
        return self.DESCUENTO_FIJO

    def get_tipo(self):
        return "Corporativo"

    def info_extra(self):
        contacto_str = f" | Contacto: {self.__contacto}" if self.__contacto else ""
        return f"Empresa: {self.__empresa}{contacto_str}"

    def to_dict(self):
        """Extiende el diccionario base con empresa y contacto."""
        datos = super().to_dict()
        datos["empresa"] = self.__empresa
        datos["contacto"] = self.__contacto
        return datos

    def __str__(self):
        return super().__str__() + f" | Empresa: {self.__empresa}"