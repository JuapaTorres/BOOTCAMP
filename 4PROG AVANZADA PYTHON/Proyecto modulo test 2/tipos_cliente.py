from cliente import Cliente

class ClienteRegular(Cliente):
    def __init__(self, cliente_id, nombre, email, puntos):
        super().__init__(cliente_id, nombre, email)
        self.__puntos = puntos

    def get_puntos(self):
        return self.__puntos

    def calcular_descuento(self):
        #0.01 para clientes regulares
        return self.__puntos * 0.01
    
class ClientePremium(Cliente):
    def __init__(self, cliente_id, nombre, email):
        super().__init__(cliente_id, nombre, email)
        
    def calcular_descuento(self):
        # Descuento premium de 20
        return 20
        
class ClienteCorporativo(Cliente):
    def __init__(self, cliente_id, nombre, email, empresa):
        super().__init__(cliente_id, nombre, email)
        self.__empresa = empresa

    def get_empresa(self):
        return self.__empresa

    def calcular_descuento(self):
        # Descuento corporativo de 30
        return 30