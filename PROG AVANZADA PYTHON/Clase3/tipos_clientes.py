class ClienteRegular():
    def __init__(self, cliente_id, nombre, email, puntos):
        self._puntos = puntos

    def calcular_descuento(self):
        return self._puntos*0.01
    
class ClientePremium():
    def __init__(self, cliente_id, nombre, email):
        pass

    def calcular_descuento(self):
        return 20
    

class ClienteCorporativo():
    def __init__(self, cliente_id, ):
        pass