from tipos_cliente import ClienteCorporativo, ClientePremium, ClienteRegular
from gestor_clientes import GestorClientes

def main():
    gestor = GestorClientes()

    cliente_regular = ClienteRegular(1, "Ana Tapia", "anatapia@gmail.com", 100)
    cliente_premium = ClientePremium(2, "Luis Soto", "luissoto@gmail.com")
    cliente_corporativo = ClienteCorporativo(3, "Juan Perez", "juanitoperez@gmail.com", "Juanito instalaciones")

    gestor.agregar(cliente_regular)
    gestor.agregar(cliente_premium)
    gestor.agregar(cliente_corporativo)

    gestor.listar()

if __name__=="__main__":
    main()