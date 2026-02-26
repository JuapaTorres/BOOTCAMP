class GestorClientes:
    def __init__(self):
        self._clientes = []

    def agregar(self, cliente):
        self._clientes.append(cliente)

    def listar(self):
        for cliente in self._clientes:
            print(f"{cliente.get_nombre()} Descuento: {cliente.calcular_descuento()}")

    def buscar(self, id_cliente):
        for cliente in self._clientes:
            if cliente.get_id() == id_cliente:
                return cliente
        return None
    
    def eliminar(self, id_cliente):
        nueva_lista = []

        for cliente in self._clientes:
            if cliente.get_id()!=id_cliente:
                nueva_lista.append()

        self._clientes = nueva_lista
        