class GestorClientes:
    def __init__(self):
        self.__clientes = []

    def agregar(self, cliente):
        self.__clientes.append(cliente)

    def get_clientes(self):
        return self.__clientes

    def set_clientes(self, lista):
        self.__clientes = lista

    def listar(self):
        for c in self.__clientes:
            print(f"{c.get_id()} - {c.get_nombre()}")

    def eliminar(self, id_cliente):
        nueva_lista = []
        for c in self.__clientes:
            if c.get_id() != id_cliente:
                nueva_lista.append(c)
        self.__clientes = nueva_lista

    def existe_id(self, id_cliente):
        for c in self.__clientes:
            if c.get_id() == id_cliente:
                return True
        return False