# =============================================================================
# archivos.py — Persistencia en JSON y CSV con finally para cierre seguro
# =============================================================================
import json
import csv
import logging
from excepciones import ArchivoError

logger = logging.getLogger(__name__)


class GestorJSON:
    """Maneja la lectura y escritura de clientes en formato JSON.
    
    Demuestra el uso de try/except/finally para leer un archivo
    y cerrarlo siempre, incluso ante errores.
    """

    def guardar(self, clientes, ruta="clientes.json"):
        """Serializa la lista de clientes a un archivo JSON.
        
        Args:
            clientes (list[Cliente]): Lista de instancias de cliente.
            ruta (str): Ruta del archivo de destino.
        
        Raises:
            ArchivoError: Si no se puede escribir el archivo.
        """
        archivo = None
        try:
            datos = [c.to_dict() for c in clientes]
            archivo = open(ruta, "w", encoding="utf-8")
            json.dump(datos, archivo, ensure_ascii=False, indent=2)
            logger.info(f"JSON guardado: {len(datos)} clientes en '{ruta}'.")
        except OSError as e:
            # Capturamos el error de I/O y lo re-lanzamos como ArchivoError
            raise ArchivoError(ruta, "escribir", str(e))
        except (TypeError, ValueError) as e:
            raise ArchivoError(ruta, "serializar", str(e))
        finally:
            # El archivo se cierra SIEMPRE, haya error o no
            if archivo and not archivo.closed:
                archivo.close()
                logger.debug(f"Archivo JSON '{ruta}' cerrado correctamente.")

    def cargar(self, ruta="clientes.json"):
        """Lee un archivo JSON y retorna una lista de diccionarios.
        
        Demuestra: leer un archivo y cerrarlo siempre con finally.
        Captura el error en la función y lo re-lanza como ArchivoError.
        
        Args:
            ruta (str): Ruta del archivo JSON a leer.
        
        Returns:
            list[dict]: Lista de diccionarios con los datos.
        
        Raises:
            ArchivoError: Si el archivo no existe o el JSON es inválido.
        """
        archivo = None
        try:
            archivo = open(ruta, "r", encoding="utf-8")
            datos = json.load(archivo)
            logger.info(f"JSON cargado: {len(datos)} registros desde '{ruta}'.")
            return datos
        except FileNotFoundError:
            # No hay datos previos — retornamos lista vacía sin error
            logger.warning(f"Archivo '{ruta}' no encontrado. Se retorna lista vacía.")
            return []
        except json.JSONDecodeError as e:
            # Capturamos y re-lanzamos hacia el exterior
            raise ArchivoError(ruta, "parsear JSON", str(e))
        except OSError as e:
            raise ArchivoError(ruta, "leer", str(e))
        finally:
            # Cierre seguro del archivo
            if archivo and not archivo.closed:
                archivo.close()
                logger.debug(f"Archivo JSON '{ruta}' cerrado en finally.")


class GestorCSV:
    """Maneja la exportación e importación de clientes en formato CSV."""

    CAMPOS = [
        "id", "tipo", "nombre", "email", "telefono",
        "direccion", "descuento", "puntos", "empresa", "contacto", "beneficios"
    ]

    def exportar(self, clientes, ruta="clientes.csv"):
        """Exporta la lista de clientes a un archivo CSV.
        
        Args:
            clientes (list[Cliente]): Lista de instancias de cliente.
            ruta (str): Ruta del archivo CSV de destino.
        
        Raises:
            ArchivoError: Si la escritura falla.
        """
        archivo = None
        try:
            archivo = open(ruta, "w", newline="", encoding="utf-8")
            writer = csv.DictWriter(
                archivo,
                fieldnames=self.CAMPOS,
                extrasaction="ignore"  # Ignorar campos extra no listados
            )
            writer.writeheader()
            for cliente in clientes:
                fila = cliente.to_dict()
                # Convertir lista de beneficios a string para CSV
                if isinstance(fila.get("beneficios"), list):
                    fila["beneficios"] = "|".join(fila["beneficios"])
                writer.writerow(fila)
            logger.info(f"CSV exportado: {len(clientes)} clientes en '{ruta}'.")
        except OSError as e:
            raise ArchivoError(ruta, "escribir CSV", str(e))
        finally:
            if archivo and not archivo.closed:
                archivo.close()
                logger.debug(f"Archivo CSV '{ruta}' cerrado correctamente.")

    def importar(self, ruta="clientes.csv"):
        """Importa clientes desde un archivo CSV.
        
        Args:
            ruta (str): Ruta del archivo CSV.
        
        Returns:
            list[dict]: Lista de diccionarios con los datos importados.
        
        Raises:
            ArchivoError: Si el archivo no existe o está malformado.
        """
        archivo = None
        try:
            archivo = open(ruta, "r", newline="", encoding="utf-8")
            reader = csv.DictReader(archivo)
            datos = list(reader)
            logger.info(f"CSV importado: {len(datos)} registros desde '{ruta}'.")
            return datos
        except FileNotFoundError:
            logger.warning(f"CSV '{ruta}' no encontrado.")
            return []
        except csv.Error as e:
            raise ArchivoError(ruta, "parsear CSV", str(e))
        except OSError as e:
            raise ArchivoError(ruta, "leer CSV", str(e))
        finally:
            if archivo and not archivo.closed:
                archivo.close()
                logger.debug(f"Archivo CSV '{ruta}' cerrado en finally.")