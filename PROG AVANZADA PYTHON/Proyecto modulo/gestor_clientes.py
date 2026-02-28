class GestorClientes:
    def __init__(self):
        self.__clientes = []

    def agregar(self, cliente):
        self.__clientes.append(cliente)

    def listar(self):
        for cliente in self.__clientes:
            print(f"Cliente: {cliente.get_nombre()} - Descuento: {cliente.calcular_descuento()}")

    def buscar(self,id_cliente):
        for cliente in self.__clientes:
            if cliente.get_id() == id_cliente:
                return cliente
        
    def eliminar(self, id_cliente):
        nueva_lista = []

        for cliente in self.__clientes:
            if cliente.get_id() != id_cliente:
                nueva_lista.append(cliente)
        
        self.__clientes = nueva_lista