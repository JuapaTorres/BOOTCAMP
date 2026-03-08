import tkinter as tk
from tkinter import messagebox
from gestor_clientes import GestorClientes
from persistencia import Persistencia
from tipos_cliente import ClienteRegular, ClientePremium, ClienteCorporativo
from excepciones import IdDuplicadoError, DatoVacioError, FormatoInvalidoError, ErrorCliente, EmailInvalidoError

class InterfazCliente:
    def __init__(self, ventana):
        self.gestor = GestorClientes()
        self.gestor.set_clientes(Persistencia.cargar())
        
        self.ventana = ventana
        self.ventana.title("Gestor clientes")
        self.ventana.geometry("500x850") 

        #SECCIÓN DE REGISTRO
        tk.Label(ventana, text="--- REGISTRO DE CLIENTE ---", font=("Arial", 10, "bold")).pack(pady=5)
        
        tk.Label(ventana, text="ID:").pack()
        self.txt_id = tk.Entry(ventana)
        self.txt_id.pack()

        tk.Label(ventana, text="Nombre:").pack()
        self.txt_nombre = tk.Entry(ventana)
        self.txt_nombre.pack()

        tk.Label(ventana, text="Email:").pack()
        self.txt_email = tk.Entry(ventana)
        self.txt_email.pack()

        tk.Label(ventana, text="Tipo:").pack()
        self.tipo_var = tk.StringVar(ventana)
        self.tipo_var.set("Regular")
        tk.OptionMenu(ventana, self.tipo_var, "Regular", "Premium", "Corporativo").pack()

        tk.Label(ventana, text="Dato Extra (Empresa):").pack()
        self.txt_extra = tk.Entry(ventana)
        self.txt_extra.pack()

        tk.Button(ventana, text="Agregar Cliente", command=self.agregar_cliente, bg="lightblue").pack(pady=10)

        #SECCIÓN DE BÚSQUEDA
        tk.Label(ventana, text="--- BÚSQUEDA ---", font=("Arial", 10, "bold")).pack(pady=5)
        tk.Label(ventana, text="Buscar por ID o Nombre:").pack()
        self.txt_buscar = tk.Entry(ventana)
        self.txt_buscar.pack()
        
        #botones de búsqueda
        frame_busqueda = tk.Frame(ventana)
        frame_busqueda.pack(pady=5)
        tk.Button(frame_busqueda, text="Buscar", command=self.buscar_cliente, bg="lightyellow").pack(side=tk.LEFT, padx=5)
        tk.Button(frame_busqueda, text="Ver Todos", command=self.actualizar_lista_visual, bg="white").pack(side=tk.LEFT, padx=5)
        

        tk.Label(ventana, text="--- LISTADO ---", font=("Arial", 10, "bold")).pack(pady=5)
        self.lista_visual = tk.Listbox(ventana, width=65, height=10)
        self.lista_visual.pack(padx=10)

        tk.Button(ventana, text="Eliminar Seleccionado", command=self.eliminar_cliente, bg="salmon").pack(pady=5)
        tk.Button(ventana, text="GUARDAR TODO EN JSON", command=self.guardar_datos, bg="lightgreen", font=("Arial", 9, "bold")).pack(pady=10)
        tk.Button(ventana, text="Exportar a Excel (CSV)", command=self.exportar_a_csv, bg="orange").pack(pady=5)
        
        self.actualizar_lista_visual()

    def agregar_cliente(self):
        try:
            if not self.txt_id.get().strip(): 
                raise DatoVacioError("ID")
            if not self.txt_nombre.get().strip(): 
                raise DatoVacioError("Nombre")
            
            # Validar que el ID sea numnúymero
            try:
                id_c = int(self.txt_id.get())
            except ValueError:
                raise FormatoInvalidoError(self.txt_id.get())

            # Validar si el ID ya existe
            if self.gestor.existe_id(id_c):
                raise IdDuplicadoError(id_c)

            nom = self.txt_nombre.get()
            mail = self.txt_email.get()
            tipo = self.tipo_var.get()
            extra = self.txt_extra.get()

            if tipo == "Regular":
                try:
                    pts = int(extra) if extra else 0
                except ValueError:
                    raise FormatoInvalidoError("Puntos (Dato Extra)")
                nuevo = ClienteRegular(id_c, nom, mail, pts)
                
            elif tipo == "Premium":
                nuevo = ClientePremium(id_c, nom, mail)
                
            elif tipo == "Corporativo":
                if not extra.strip(): 
                    raise DatoVacioError("Empresa (Dato Extra)")
                nuevo = ClienteCorporativo(id_c, nom, mail, extra)

            self.gestor.agregar(nuevo)
            self.actualizar_lista_visual()
            self.limpiar_campos()
            messagebox.showinfo("Éxito", f"Cliente {tipo} registrado correctamente.")

        except ErrorCliente as e:
            messagebox.showerror("Error de Validación", e.mensaje)
            
        except Exception as e:
            messagebox.showerror("Error Inesperado", f"Ocurrió un problema: {str(e)}")

    def buscar_cliente(self):
        criterio = self.txt_buscar.get().lower()
        if not criterio:
            messagebox.showwarning("Atención", "Ingresa un ID o nombre para buscar.")
            return

        # Limpiamos la lista para mostrar solo resultados
        self.lista_visual.delete(0, tk.END)
        encontrado = False

        for c in self.gestor.get_clientes():
            # Buscamos por ID
            if criterio == str(c.get_id()) or criterio in c.get_nombre().lower():
                info = f"ID: {c.get_id()} | {c.get_nombre()} | Desc: ${c.calcular_descuento()}"
                self.lista_visual.insert(tk.END, info)
                encontrado = True
        
        if not encontrado:
            messagebox.showinfo("Búsqueda", "No se encontraron coincidencias.")
            self.actualizar_lista_visual()

    def guardar_datos(self):
        Persistencia.guardar(self.gestor.get_clientes())
        messagebox.showinfo("JSON", "Archivo 'clientes.json' guardado correctamente.")

    def exportar_a_csv(self):
        exito = Persistencia.exportar_csv(self.gestor.get_clientes())
        if exito:
            messagebox.showinfo("Exportar", "Se ha creado el archivo 'reporte_clientes.csv' con éxito.")
        else:
            messagebox.showerror("Error", "No se pudo exportar el archivo.")

    def eliminar_cliente(self):
        seleccion = self.lista_visual.curselection()
        if not seleccion:
            messagebox.showwarning("Atención", "Selecciona un cliente de la lista.")
            return
            
        texto = self.lista_visual.get(seleccion[0])
        id_a_borrar = int(texto.split("|")[0].replace("ID: ", "").strip())
        
        self.gestor.eliminar(id_a_borrar)
        self.actualizar_lista_visual()
        messagebox.showinfo("Eliminado", f"ID {id_a_borrar} eliminado de la lista local (no olvides guardar).")

    def actualizar_lista_visual(self):
        self.lista_visual.delete(0, tk.END)
        self.txt_buscar.delete(0, tk.END) #Limpiar buscador al refrescar
        for c in self.gestor.get_clientes():
            info = f"ID: {c.get_id()} | {c.get_nombre()} | Desc: ${c.calcular_descuento()}"
            self.lista_visual.insert(tk.END, info)

    def limpiar_campos(self):
        self.txt_id.delete(0, tk.END)
        self.txt_nombre.delete(0, tk.END)
        self.txt_email.delete(0, tk.END)
        self.txt_extra.delete(0, tk.END)