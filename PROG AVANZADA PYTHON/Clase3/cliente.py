class Cliente():
    def __init__(self, cliente_id, nombre, email):
        self._id = cliente_id
        self._nombre = nombre
        self._email = email

    def get_id(self):
        return self._id
    
    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, nombre):
        self._nombre = nombre

    def calcular_descuento(self):
        return None
    