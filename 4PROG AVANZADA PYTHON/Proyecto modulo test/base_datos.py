# =============================================================================
# base_datos.py — Persistencia SQLite con manejo de errores y finally
# =============================================================================
import sqlite3
import logging
from excepciones import BaseDatosError

logger = logging.getLogger(__name__)


class BaseDatos:
    """Gestiona la conexión y operaciones CRUD sobre SQLite.
    
    Usa el bloque finally para garantizar el cierre seguro de la conexión
    incluso cuando ocurren errores.
    
    Args:
        ruta_db (str): Ruta al archivo .db de SQLite.
    """

    def __init__(self, ruta_db="gic_clientes.db"):
        self.__ruta = ruta_db
        self.__conexion = None
        self._inicializar_tabla()

    def _conectar(self):
        """Abre la conexión a SQLite.
        
        Returns:
            sqlite3.Connection: Conexión activa.
        
        Raises:
            BaseDatosError: Si no se puede conectar.
        """
        try:
            conexion = sqlite3.connect(self.__ruta)
            conexion.row_factory = sqlite3.Row  # Permite acceso por nombre de columna
            return conexion
        except sqlite3.Error as e:
            raise BaseDatosError("conectar", str(e))

    def _inicializar_tabla(self):
        """Crea la tabla 'clientes' si no existe.
        Usa finally para cerrar la conexión siempre.
        
        Raises:
            BaseDatosError: Si falla la creación de la tabla.
        """
        conexion = None
        try:
            conexion = self._conectar()
            cursor = conexion.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS clientes (
                    id          INTEGER PRIMARY KEY,
                    tipo        TEXT    NOT NULL,
                    nombre      TEXT    NOT NULL,
                    email       TEXT    NOT NULL UNIQUE,
                    telefono    TEXT    DEFAULT '',
                    direccion   TEXT    DEFAULT '',
                    puntos      INTEGER DEFAULT 0,
                    empresa     TEXT    DEFAULT '',
                    contacto    TEXT    DEFAULT '',
                    beneficios  TEXT    DEFAULT ''
                )
            """)
            conexion.commit()
            logger.info("Tabla 'clientes' inicializada correctamente.")
        except sqlite3.Error as e:
            raise BaseDatosError("inicializar_tabla", str(e))
        finally:
            # El bloque finally garantiza que la conexión se cierra SIEMPRE
            if conexion:
                conexion.close()
                logger.debug("Conexión cerrada tras inicialización.")

    def guardar_cliente(self, cliente):
        """Inserta o actualiza un cliente en la base de datos.
        
        Usa INSERT OR REPLACE para manejar duplicados por ID.
        
        Args:
            cliente (Cliente): Instancia de cualquier subclase de Cliente.
        
        Raises:
            BaseDatosError: Si la operación de escritura falla.
        """
        conexion = None
        try:
            datos = cliente.to_dict()
            conexion = self._conectar()
            cursor = conexion.cursor()
            cursor.execute("""
                INSERT OR REPLACE INTO clientes
                    (id, tipo, nombre, email, telefono, direccion,
                     puntos, empresa, contacto, beneficios)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                datos.get("id"),
                datos.get("tipo", ""),
                datos.get("nombre", ""),
                datos.get("email", ""),
                datos.get("telefono", ""),
                datos.get("direccion", ""),
                datos.get("puntos", 0),
                datos.get("empresa", ""),
                datos.get("contacto", ""),
                ",".join(datos.get("beneficios", []))
            ))
            conexion.commit()
            logger.info(f"Cliente ID={datos['id']} guardado en SQLite.")
        except sqlite3.IntegrityError as e:
            raise BaseDatosError("guardar_cliente", f"Email duplicado: {e}")
        except sqlite3.Error as e:
            raise BaseDatosError("guardar_cliente", str(e))
        finally:
            if conexion:
                conexion.close()

    def obtener_todos(self):
        """Lee todos los clientes de la base de datos.
        
        Returns:
            list[dict]: Lista de diccionarios con los datos de cada cliente.
        
        Raises:
            BaseDatosError: Si la lectura falla.
        """
        conexion = None
        try:
            conexion = self._conectar()
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM clientes ORDER BY id")
            filas = cursor.fetchall()
            # Convertir Row objects a diccionarios
            resultado = [dict(fila) for fila in filas]
            logger.info(f"Se leyeron {len(resultado)} clientes de SQLite.")
            return resultado
        except sqlite3.Error as e:
            raise BaseDatosError("obtener_todos", str(e))
        finally:
            if conexion:
                conexion.close()

    def obtener_por_id(self, cliente_id):
        """Busca un cliente por su ID.
        
        Args:
            cliente_id (int): ID del cliente a buscar.
        
        Returns:
            dict | None: Datos del cliente o None si no existe.
        
        Raises:
            BaseDatosError: Si la consulta falla.
        """
        conexion = None
        try:
            conexion = self._conectar()
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM clientes WHERE id = ?", (cliente_id,))
            fila = cursor.fetchone()
            return dict(fila) if fila else None
        except sqlite3.Error as e:
            raise BaseDatosError("obtener_por_id", str(e))
        finally:
            if conexion:
                conexion.close()

    def eliminar_cliente(self, cliente_id):
        """Elimina un cliente de la base de datos por su ID.
        
        Args:
            cliente_id (int): ID del cliente a eliminar.
        
        Returns:
            bool: True si se eliminó, False si no existía.
        
        Raises:
            BaseDatosError: Si la operación falla.
        """
        conexion = None
        try:
            conexion = self._conectar()
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM clientes WHERE id = ?", (cliente_id,))
            conexion.commit()
            eliminado = cursor.rowcount > 0
            if eliminado:
                logger.info(f"Cliente ID={cliente_id} eliminado de SQLite.")
            return eliminado
        except sqlite3.Error as e:
            raise BaseDatosError("eliminar_cliente", str(e))
        finally:
            if conexion:
                conexion.close()