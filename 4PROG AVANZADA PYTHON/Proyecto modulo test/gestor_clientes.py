# =============================================================================
# gestor_clientes.py — CRUD completo con validaciones y persistencia
# =============================================================================
import logging
from tipos_cliente import ClienteRegular, ClientePremium, ClienteCorporativo
from excepciones import (
    ClienteNoEncontradoError, ClienteDuplicadoError,
    GICError, BaseDatosError, ArchivoError
)
from base_datos import BaseDatos
from archivos import GestorJSON, GestorCSV

logger = logging.getLogger(__name__)


class GestorClientes:
    """Gestiona el ciclo de vida de los clientes: CRUD + persistencia.
    
    Mantiene una lista en memoria como caché y sincroniza con SQLite,
    JSON y CSV según se solicite.
    
    Attributes:
        __clientes (list[Cliente]): Caché en memoria.
        __db (BaseDatos): Gestor de SQLite.
        __json (GestorJSON): Gestor de archivos JSON.
        __csv (GestorCSV): Gestor de archivos CSV.
    """

    def __init__(self, ruta_db="gic_clientes.db"):
        self.__clientes = []
        self.__db = BaseDatos(ruta_db)
        self.__json = GestorJSON()
        self.__csv = GestorCSV()
        self._cargar_desde_db()

    # ── Carga inicial ──────────────────────────────────────────────────────

    def _cargar_desde_db(self):
        """Carga los clientes desde SQLite al iniciar el gestor.
        
        Convierte las filas de la DB en instancias de la subclase correcta.
        Errores de carga se registran en el log sin detener la aplicación.
        """
        try:
            filas = self.__db.obtener_todos()
            for fila in filas:
                cliente = self._fila_a_cliente(fila)
                if cliente:
                    self.__clientes.append(cliente)
            logger.info(f"Gestor iniciado con {len(self.__clientes)} clientes.")
        except BaseDatosError as e:
            logger.error(f"No se pudo cargar desde DB: {e}")

    def _fila_a_cliente(self, fila):
        """Convierte un dict (fila de DB o JSON) en la instancia correcta.
        
        Args:
            fila (dict): Datos del cliente.
        
        Returns:
            Cliente | None: Instancia de subclase o None si el tipo es desconocido.
        """
        try:
            tipo = fila.get("tipo", "")
            cid = int(fila["id"])
            nombre = fila["nombre"]
            email = fila["email"]
            telefono = fila.get("telefono", "")
            direccion = fila.get("direccion", "")

            if tipo == "Regular":
                return ClienteRegular(
                    cid, nombre, email,
                    puntos=int(fila.get("puntos", 0)),
                    telefono=telefono, direccion=direccion
                )
            elif tipo == "Premium":
                beneficios_raw = fila.get("beneficios", "")
                beneficios = (
                    beneficios_raw.split(",") if isinstance(beneficios_raw, str) and beneficios_raw
                    else beneficios_raw if isinstance(beneficios_raw, list)
                    else []
                )
                return ClientePremium(
                    cid, nombre, email,
                    beneficios=beneficios,
                    telefono=telefono, direccion=direccion
                )
            elif tipo == "Corporativo":
                return ClienteCorporativo(
                    cid, nombre, email,
                    empresa=fila.get("empresa", "Empresa"),
                    contacto=fila.get("contacto", ""),
                    telefono=telefono, direccion=direccion
                )
            else:
                logger.warning(f"Tipo de cliente desconocido: '{tipo}', se omite.")
                return None
        except Exception as e:
            logger.error(f"Error al reconstruir cliente desde fila {fila}: {e}")
            return None

    # ── CRUD ───────────────────────────────────────────────────────────────

    def agregar(self, cliente):
        """Agrega un cliente al sistema (memoria + SQLite).
        
        Valida que no exista duplicado por ID o email.
        
        Args:
            cliente (Cliente): Instancia a agregar.
        
        Raises:
            ClienteDuplicadoError: Si ya existe un cliente con ese ID o email.
            BaseDatosError: Si falla la escritura en DB.
        """
        # Verificar duplicados
        for c in self.__clientes:
            if c.get_id() == cliente.get_id():
                raise ClienteDuplicadoError("ID", cliente.get_id())
            if c.get_email() == cliente.get_email():
                raise ClienteDuplicadoError("email", cliente.get_email())

        self.__clientes.append(cliente)

        try:
            self.__db.guardar_cliente(cliente)
        except BaseDatosError as e:
            # Revertir el agregado en memoria si falla la DB
            self.__clientes.remove(cliente)
            raise

        logger.info(f"Cliente '{cliente.get_nombre()}' (ID={cliente.get_id()}) agregado.")

    def buscar(self, cliente_id):
        """Busca un cliente por su ID.
        
        Args:
            cliente_id (int): ID del cliente.
        
        Returns:
            Cliente: La instancia encontrada.
        
        Raises:
            ClienteNoEncontradoError: Si no existe el ID.
        """
        for cliente in self.__clientes:
            if cliente.get_id() == cliente_id:
                return cliente
        raise ClienteNoEncontradoError(cliente_id)

    def buscar_por_email(self, email):
        """Busca un cliente por su email (case-insensitive).
        
        Args:
            email (str): Email a buscar.
        
        Returns:
            Cliente | None: La instancia encontrada o None.
        """
        email = email.strip().lower()
        for cliente in self.__clientes:
            if cliente.get_email() == email:
                return cliente
        return None

    def editar(self, cliente_id, **kwargs):
        """Edita los atributos de un cliente existente.
        
        Acepta: nombre, email, telefono, direccion y campos específicos
        de cada tipo (puntos, empresa, contacto, beneficios).
        
        Args:
            cliente_id (int): ID del cliente a editar.
            **kwargs: Campos y nuevos valores.
        
        Raises:
            ClienteNoEncontradoError: Si el cliente no existe.
            ValidacionError: Si algún valor es inválido.
            BaseDatosError: Si falla la actualización en DB.
        """
        cliente = self.buscar(cliente_id)  # Lanza ClienteNoEncontradoError si no existe

        # Atributos comunes de la clase base
        if "nombre" in kwargs:
            cliente.set_nombre(kwargs["nombre"])
        if "email" in kwargs:
            cliente.set_email(kwargs["email"])
        if "telefono" in kwargs:
            cliente.set_telefono(kwargs["telefono"])
        if "direccion" in kwargs:
            cliente.set_direccion(kwargs["direccion"])

        # Atributos específicos según el tipo
        if isinstance(cliente, ClienteRegular) and "puntos" in kwargs:
            cliente.set_puntos(kwargs["puntos"])
        if isinstance(cliente, ClienteCorporativo):
            if "empresa" in kwargs:
                cliente.set_empresa(kwargs["empresa"])
            if "contacto" in kwargs:
                cliente.set_contacto(kwargs["contacto"])
        if isinstance(cliente, ClientePremium) and "beneficio" in kwargs:
            cliente.agregar_beneficio(kwargs["beneficio"])

        # Persistir cambios
        try:
            self.__db.guardar_cliente(cliente)
        except BaseDatosError as e:
            logger.error(f"Error al actualizar cliente ID={cliente_id} en DB: {e}")
            raise

        logger.info(f"Cliente ID={cliente_id} actualizado.")

    def eliminar(self, cliente_id):
        """Elimina un cliente del sistema (memoria + SQLite).
        
        Args:
            cliente_id (int): ID del cliente a eliminar.
        
        Raises:
            ClienteNoEncontradoError: Si el cliente no existe.
            BaseDatosError: Si falla la eliminación en DB.
        """
        cliente = self.buscar(cliente_id)  # Valida existencia
        self.__clientes.remove(cliente)

        try:
            self.__db.eliminar_cliente(cliente_id)
        except BaseDatosError as e:
            # Revertir si falla la DB
            self.__clientes.append(cliente)
            raise

        logger.info(f"Cliente ID={cliente_id} eliminado.")

    def listar(self):
        """Retorna la lista completa de clientes en memoria.
        
        Returns:
            list[Cliente]: Copia de la lista de clientes.
        """
        return list(self.__clientes)

    def cantidad(self):
        """Retorna la cantidad de clientes registrados."""
        return len(self.__clientes)

    # ── Persistencia JSON/CSV ──────────────────────────────────────────────

    def exportar_json(self, ruta="clientes.json"):
        """Exporta todos los clientes a un archivo JSON.
        
        Args:
            ruta (str): Ruta del archivo de destino.
        
        Raises:
            ArchivoError: Si la escritura falla.
        """
        self.__json.guardar(self.__clientes, ruta)
        logger.info(f"Exportación JSON completada: '{ruta}'.")

    def importar_json(self, ruta="clientes.json"):
        """Importa clientes desde un archivo JSON y los agrega al sistema.
        
        Args:
            ruta (str): Ruta del archivo JSON.
        
        Returns:
            int: Cantidad de clientes importados.
        
        Raises:
            ArchivoError: Si la lectura falla.
        """
        datos = self.__json.cargar(ruta)
        importados = 0
        for fila in datos:
            try:
                cliente = self._fila_a_cliente(fila)
                if cliente:
                    self.agregar(cliente)
                    importados += 1
            except (ClienteDuplicadoError, GICError) as e:
                logger.warning(f"Cliente omitido al importar: {e}")
        return importados

    def exportar_csv(self, ruta="clientes.csv"):
        """Exporta todos los clientes a un archivo CSV.
        
        Args:
            ruta (str): Ruta del archivo CSV.
        
        Raises:
            ArchivoError: Si la escritura falla.
        """
        self.__csv.exportar(self.__clientes, ruta)

    def importar_csv(self, ruta="clientes.csv"):
        """Importa clientes desde un archivo CSV.
        
        Args:
            ruta (str): Ruta del archivo CSV.
        
        Returns:
            int: Cantidad de clientes importados.
        """
        datos = self.__csv.importar(ruta)
        importados = 0
        for fila in datos:
            try:
                cliente = self._fila_a_cliente(fila)
                if cliente:
                    self.agregar(cliente)
                    importados += 1
            except (ClienteDuplicadoError, GICError) as e:
                logger.warning(f"Fila CSV omitida: {e}")
        return importados