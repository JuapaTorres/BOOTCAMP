# =============================================================================
# main.py — Punto de entrada del GIC
# =============================================================================
import logging
import sys

# ── Configuración del sistema de logs ─────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler("gic.log", encoding="utf-8"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)


def demo_consola():
    """
    Demostración en consola del sistema GIC.
    Muestra herencia, polimorfismo, excepciones y validaciones.
    Se puede ejecutar sin GUI para pruebas.
    """
    from gestor_clientes import GestorClientes
    from tipos_cliente import ClienteRegular, ClientePremium, ClienteCorporativo
    from excepciones import (
        ClienteNoEncontradoError, ClienteDuplicadoError,
        EmailInvalidoError, NombreInvalidoError
    )

    print("\n" + "="*60)
    print("   GIC — Gestor Inteligente de Clientes (Demo Consola)")
    print("="*60)

    gestor = GestorClientes("demo_gic.db")

    # ── 1. Crear clientes con validaciones ────────────────────────────────
    print("\n📋 Creando clientes...")
    try:
        c1 = ClienteRegular(1, "Ana Tapia", "anatapia@gmail.com",
                            puntos=500, telefono="1145678900")
        c2 = ClientePremium(2, "Luis Soto", "luissoto@gmail.com",
                            beneficios=["Envío gratis", "Soporte 24/7"])
        c3 = ClienteCorporativo(3, "Juan Pérez", "juanitoperez@gmail.com",
                                empresa="Juanito Instalaciones",
                                contacto="María Rodríguez",
                                telefono="01112345678")
        gestor.agregar(c1)
        gestor.agregar(c2)
        gestor.agregar(c3)
        print(f"   ✅ {c1}")
        print(f"   ✅ {c2}")
        print(f"   ✅ {c3}")
    except Exception as e:
        print(f"   ❌ {e}")

    # ── 2. Polimorfismo: calcular_descuento() en cada tipo ─────────────────
    print("\n💰 Polimorfismo — calcular_descuento():")
    for cliente in gestor.listar():
        print(f"   [{cliente.get_tipo():12}] {cliente.get_nombre():20} "
              f"→ {cliente.calcular_descuento():.1f}% descuento")
        print(f"              Info extra: {cliente.info_extra()}")

    # ── 3. __str__ y __eq__ ────────────────────────────────────────────────
    print("\n🔍 Métodos especiales:")
    print(f"   __str__  → {c1}")
    print(f"   __repr__ → {repr(c1)}")
    print(f"   c1 == c2 → {c1 == c2}  (distinto ID y email)")
    c1_copia = ClienteRegular(1, "Ana Tapia", "anatapia@gmail.com", 100)
    print(f"   c1 == c1_copia → {c1 == c1_copia}  (mismo ID)")

    # ── 4. Validaciones con isinstance y raise ─────────────────────────────
    print("\n⚠️  Validaciones y excepciones:")

    # Email inválido
    try:
        ClienteRegular(10, "Test", "no-es-un-email")
    except EmailInvalidoError as e:
        print(f"   EmailInvalidoError capturada: {e}")

    # Nombre inválido (contiene números)
    try:
        ClienteRegular(11, "Ana123", "test@test.com")
    except NombreInvalidoError as e:
        print(f"   NombreInvalidoError capturada: {e}")

    # Cliente duplicado
    try:
        duplicado = ClienteRegular(1, "Otro", "otro@mail.com")
        gestor.agregar(duplicado)
    except ClienteDuplicadoError as e:
        print(f"   ClienteDuplicadoError capturada: {e}")

    # Cliente no encontrado
    try:
        gestor.buscar(999)
    except ClienteNoEncontradoError as e:
        print(f"   ClienteNoEncontradoError capturada: {e}")

    # ── 5. Edición ─────────────────────────────────────────────────────────
    print("\n✏️  Editando cliente ID=1...")
    try:
        gestor.editar(1, nombre="Ana María Tapia", telefono="1198765432")
        cliente_editado = gestor.buscar(1)
        print(f"   {cliente_editado}")
    except Exception as e:
        print(f"   ❌ {e}")

    # ── 6. Exportar JSON y CSV ─────────────────────────────────────────────
    print("\n💾 Exportando datos...")
    try:
        gestor.exportar_json("demo_clientes.json")
        print("   ✅ JSON exportado: demo_clientes.json")
        gestor.exportar_csv("demo_clientes.csv")
        print("   ✅ CSV exportado: demo_clientes.csv")
    except Exception as e:
        print(f"   ❌ Error al exportar: {e}")

    # ── 7. Eliminar ────────────────────────────────────────────────────────
    print("\n🗑️  Eliminando cliente ID=3...")
    try:
        gestor.eliminar(3)
        print(f"   ✅ Eliminado. Clientes restantes: {gestor.cantidad()}")
    except ClienteNoEncontradoError as e:
        print(f"   ❌ {e}")

    print("\n" + "="*60)
    print("   Demo finalizada. Revisá gic.log para el detalle completo.")
    print("="*60 + "\n")


def main():
    """
    Punto de entrada principal.
    Ejecuta la GUI si Tkinter está disponible, o la demo en consola.
    """
    # Intentar lanzar la GUI
    try:
        from gui import iniciar_gui
        logger.info("Iniciando GIC con interfaz gráfica...")
        iniciar_gui()
    except Exception as e:
        logger.warning(f"No se pudo iniciar la GUI: {e}")
        logger.info("Iniciando demo en modo consola...")
        demo_consola()


if __name__ == "__main__":
    main()