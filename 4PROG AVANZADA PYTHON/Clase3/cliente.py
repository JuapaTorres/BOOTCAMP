class Cliente:
    def __init__(self, cliente_id, nombre, email):
        self.__id = cliente_id
        self.__nombre = nombre
        self.__email = email

    def get_id(self):
        return self.__id
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def calcular_descuento(self):
        return None
    