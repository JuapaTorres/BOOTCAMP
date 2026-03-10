# =============================================================================
# gui.py — Interfaz gráfica Tkinter para el GIC
# =============================================================================
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import logging

from gestor_clientes import GestorClientes
from tipos_cliente import ClienteRegular, ClientePremium, ClienteCorporativo
from excepciones import (
    GICError, ValidacionError, ClienteNoEncontradoError,
    ClienteDuplicadoError, EmailInvalidoError, TelefonoInvalidoError,
    DireccionInvalidaError, NombreInvalidoError
)

logger = logging.getLogger(__name__)

# ── Paleta de colores ──────────────────────────────────────────────────────
COLOR_BG         = "#1e1e2e"
COLOR_PANEL      = "#2a2a3e"
COLOR_ACENTO     = "#7c3aed"        # Violeta
COLOR_ACENTO2    = "#06b6d4"        # Cyan
COLOR_TEXTO      = "#e2e8f0"
COLOR_TEXTO_SUB  = "#94a3b8"
COLOR_ENTRADA    = "#0f172a"
COLOR_EXITO      = "#10b981"
COLOR_ERROR      = "#ef4444"
COLOR_WARNING    = "#f59e0b"
COLOR_REGULAR    = "#3b82f6"
COLOR_PREMIUM    = "#a855f7"
COLOR_CORP       = "#f97316"

FONT_TITULO   = ("Segoe UI", 20, "bold")
FONT_SUBTITULO= ("Segoe UI", 13, "bold")
FONT_NORMAL   = ("Segoe UI", 11)
FONT_SMALL    = ("Segoe UI", 9)
FONT_MONO     = ("Consolas", 10)


class AplicacionGIC(tk.Tk):
    """Ventana principal de la aplicación GIC."""

    def __init__(self):
        super().__init__()
        self.title("GIC — Gestor Inteligente de Clientes")
        self.geometry("1100x700")
        self.minsize(900, 600)
        self.configure(bg=COLOR_BG)
        self.resizable(True, True)

        self.gestor = GestorClientes()

        self._configurar_estilos()
        self._construir_ui()
        self._actualizar_tabla()

    # ── Estilos ────────────────────────────────────────────────────────────

    def _configurar_estilos(self):
        estilo = ttk.Style(self)
        estilo.theme_use("clam")

        estilo.configure("Treeview",
            background=COLOR_PANEL, foreground=COLOR_TEXTO,
            fieldbackground=COLOR_PANEL, rowheight=28,
            font=FONT_NORMAL, borderwidth=0
        )
        estilo.configure("Treeview.Heading",
            background=COLOR_ACENTO, foreground="white",
            font=("Segoe UI", 11, "bold"), relief="flat"
        )
        estilo.map("Treeview",
            background=[("selected", COLOR_ACENTO)],
            foreground=[("selected", "white")]
        )
        estilo.configure("TNotebook", background=COLOR_BG, borderwidth=0)
        estilo.configure("TNotebook.Tab",
            background=COLOR_PANEL, foreground=COLOR_TEXTO_SUB,
            padding=[16, 8], font=FONT_NORMAL
        )
        estilo.map("TNotebook.Tab",
            background=[("selected", COLOR_ACENTO)],
            foreground=[("selected", "white")]
        )
        estilo.configure("TCombobox",
            fieldbackground=COLOR_ENTRADA, background=COLOR_PANEL,
            foreground=COLOR_TEXTO, selectbackground=COLOR_ACENTO
        )

    # ── Construcción UI ────────────────────────────────────────────────────

    def _construir_ui(self):
        # Header
        header = tk.Frame(self, bg=COLOR_PANEL, height=60)
        header.pack(fill="x", side="top")
        header.pack_propagate(False)

        tk.Label(header, text="⚡ GIC", font=FONT_TITULO,
                 bg=COLOR_PANEL, fg=COLOR_ACENTO).pack(side="left", padx=20, pady=10)
        tk.Label(header, text="Gestor Inteligente de Clientes",
                 font=("Segoe UI", 12), bg=COLOR_PANEL, fg=COLOR_TEXTO_SUB
                 ).pack(side="left", pady=10)

        self._lbl_estado = tk.Label(header, text="", font=FONT_SMALL,
                                    bg=COLOR_PANEL, fg=COLOR_EXITO)
        self._lbl_estado.pack(side="right", padx=20)

        # Tabs
        self._tabs = ttk.Notebook(self)
        self._tabs.pack(fill="both", expand=True, padx=10, pady=10)

        self._tab_lista    = tk.Frame(self._tabs, bg=COLOR_BG)
        self._tab_agregar  = tk.Frame(self._tabs, bg=COLOR_BG)
        self._tab_editar   = tk.Frame(self._tabs, bg=COLOR_BG)
        self._tab_exportar = tk.Frame(self._tabs, bg=COLOR_BG)

        self._tabs.add(self._tab_lista,    text="📋 Clientes")
        self._tabs.add(self._tab_agregar,  text="➕ Agregar")
        self._tabs.add(self._tab_editar,   text="✏️ Editar / Eliminar")
        self._tabs.add(self._tab_exportar, text="💾 Exportar / Importar")

        self._construir_tab_lista()
        self._construir_tab_agregar()
        self._construir_tab_editar()
        self._construir_tab_exportar()

    # ── Tab: Lista ─────────────────────────────────────────────────────────

    def _construir_tab_lista(self):
        frame = self._tab_lista

        # Barra de búsqueda
        barra = tk.Frame(frame, bg=COLOR_BG)
        barra.pack(fill="x", padx=15, pady=(15, 5))
        tk.Label(barra, text="🔍 Buscar:", font=FONT_NORMAL,
                 bg=COLOR_BG, fg=COLOR_TEXTO).pack(side="left")
        self._var_busqueda = tk.StringVar()
        self._var_busqueda.trace_add("write", lambda *a: self._filtrar_tabla())
        tk.Entry(barra, textvariable=self._var_busqueda, font=FONT_NORMAL,
                 bg=COLOR_ENTRADA, fg=COLOR_TEXTO, insertbackground=COLOR_TEXTO,
                 relief="flat", width=30).pack(side="left", padx=10)

        # Contadores
        self._lbl_contador = tk.Label(barra, text="", font=FONT_SMALL,
                                      bg=COLOR_BG, fg=COLOR_TEXTO_SUB)
        self._lbl_contador.pack(side="right")

        # Tabla
        cols = ("ID", "Tipo", "Nombre", "Email", "Teléfono", "Descuento", "Info Extra")
        self._tabla = ttk.Treeview(frame, columns=cols, show="headings", selectmode="browse")

        anchos = {"ID": 50, "Tipo": 90, "Nombre": 160, "Email": 200,
                  "Teléfono": 110, "Descuento": 80, "Info Extra": 250}
        for col in cols:
            self._tabla.heading(col, text=col)
            self._tabla.column(col, width=anchos.get(col, 100), anchor="w")

        # Tags de color por tipo
        self._tabla.tag_configure("Regular",     background="#1e3a5f", foreground=COLOR_TEXTO)
        self._tabla.tag_configure("Premium",     background="#2d1f5e", foreground=COLOR_TEXTO)
        self._tabla.tag_configure("Corporativo", background="#3d1f0d", foreground=COLOR_TEXTO)

        scroll_y = ttk.Scrollbar(frame, orient="vertical", command=self._tabla.yview)
        scroll_x = ttk.Scrollbar(frame, orient="horizontal", command=self._tabla.xview)
        self._tabla.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

        self._tabla.pack(fill="both", expand=True, padx=15, pady=5)
        scroll_y.pack(side="right", fill="y")
        scroll_x.pack(side="bottom", fill="x")

        # Botón actualizar
        tk.Button(frame, text="🔄 Actualizar lista", font=FONT_NORMAL,
                  bg=COLOR_ACENTO2, fg="white", relief="flat", padx=10,
                  command=self._actualizar_tabla).pack(pady=8)

    # ── Tab: Agregar ───────────────────────────────────────────────────────

    def _construir_tab_agregar(self):
        frame = self._tab_agregar
        contenedor = tk.Frame(frame, bg=COLOR_PANEL, padx=30, pady=20)
        contenedor.pack(expand=True, padx=40, pady=30)

        tk.Label(contenedor, text="Nuevo Cliente", font=FONT_SUBTITULO,
                 bg=COLOR_PANEL, fg=COLOR_TEXTO).grid(row=0, column=0, columnspan=2,
                                                       sticky="w", pady=(0, 15))

        campos = [
            ("ID*", "id"), ("Nombre*", "nombre"), ("Email*", "email"),
            ("Teléfono", "telefono"), ("Dirección", "direccion")
        ]
        self._vars_agregar = {}
        for i, (label, key) in enumerate(campos, start=1):
            tk.Label(contenedor, text=label, font=FONT_NORMAL,
                     bg=COLOR_PANEL, fg=COLOR_TEXTO_SUB).grid(row=i, column=0, sticky="w", pady=4)
            var = tk.StringVar()
            self._vars_agregar[key] = var
            tk.Entry(contenedor, textvariable=var, font=FONT_NORMAL, width=32,
                     bg=COLOR_ENTRADA, fg=COLOR_TEXTO, insertbackground=COLOR_TEXTO,
                     relief="flat").grid(row=i, column=1, padx=10, pady=4)

        # Tipo de cliente
        fila_tipo = len(campos) + 1
        tk.Label(contenedor, text="Tipo*", font=FONT_NORMAL,
                 bg=COLOR_PANEL, fg=COLOR_TEXTO_SUB).grid(row=fila_tipo, column=0, sticky="w", pady=4)
        self._var_tipo = tk.StringVar(value="Regular")
        combo = ttk.Combobox(contenedor, textvariable=self._var_tipo, state="readonly",
                             values=["Regular", "Premium", "Corporativo"], width=30, font=FONT_NORMAL)
        combo.grid(row=fila_tipo, column=1, padx=10, pady=4)
        combo.bind("<<ComboboxSelected>>", self._on_tipo_cambio)

        # Campo extra dinámico
        self._lbl_extra = tk.Label(contenedor, text="Puntos", font=FONT_NORMAL,
                                   bg=COLOR_PANEL, fg=COLOR_TEXTO_SUB)
        self._lbl_extra.grid(row=fila_tipo + 1, column=0, sticky="w", pady=4)
        self._var_extra = tk.StringVar()
        self._entry_extra = tk.Entry(contenedor, textvariable=self._var_extra, font=FONT_NORMAL,
                                     width=32, bg=COLOR_ENTRADA, fg=COLOR_TEXTO,
                                     insertbackground=COLOR_TEXTO, relief="flat")
        self._entry_extra.grid(row=fila_tipo + 1, column=1, padx=10, pady=4)

        # Botón guardar
        tk.Button(contenedor, text="✅ Guardar cliente", font=FONT_NORMAL,
                  bg=COLOR_ACENTO, fg="white", relief="flat", padx=15, pady=6,
                  command=self._guardar_nuevo).grid(row=fila_tipo + 2, column=0,
                                                     columnspan=2, pady=20)

    def _on_tipo_cambio(self, event=None):
        """Actualiza el campo extra según el tipo de cliente."""
        tipo = self._var_tipo.get()
        labels = {"Regular": "Puntos", "Premium": "Beneficio (opcional)", "Corporativo": "Empresa*"}
        self._lbl_extra.config(text=labels.get(tipo, ""))
        self._var_extra.set("")

    def _guardar_nuevo(self):
        """Crea y guarda un nuevo cliente con manejo completo de errores."""
        try:
            cid_str = self._vars_agregar["id"].get().strip()
            if not cid_str.isdigit():
                raise ValueError("El ID debe ser un número entero positivo.")
            cid = int(cid_str)

            nombre   = self._vars_agregar["nombre"].get()
            email    = self._vars_agregar["email"].get()
            telefono = self._vars_agregar["telefono"].get()
            direccion= self._vars_agregar["direccion"].get()
            tipo     = self._var_tipo.get()
            extra    = self._var_extra.get().strip()

            if tipo == "Regular":
                puntos = int(extra) if extra.isdigit() else 0
                cliente = ClienteRegular(cid, nombre, email, puntos, telefono, direccion)
            elif tipo == "Premium":
                beneficios = [extra] if extra else []
                cliente = ClientePremium(cid, nombre, email, beneficios, telefono, direccion)
            elif tipo == "Corporativo":
                if not extra:
                    raise ValueError("El nombre de empresa es obligatorio para clientes corporativos.")
                cliente = ClienteCorporativo(cid, nombre, email, extra, "", telefono, direccion)

            self.gestor.agregar(cliente)
            self._mostrar_estado(f"✅ Cliente '{nombre}' agregado correctamente.", COLOR_EXITO)
            self._actualizar_tabla()
            self._limpiar_formulario_agregar()

        except (EmailInvalidoError, TelefonoInvalidoError,
                DireccionInvalidaError, NombreInvalidoError) as e:
            messagebox.showerror("Error de validación", str(e))
        except ClienteDuplicadoError as e:
            messagebox.showerror("Cliente duplicado", str(e))
        except ValidacionError as e:
            messagebox.showerror("Error de validación", str(e))
        except ValueError as e:
            messagebox.showerror("Valor inválido", str(e))
        except GICError as e:
            messagebox.showerror("Error del sistema", str(e))

    def _limpiar_formulario_agregar(self):
        for var in self._vars_agregar.values():
            var.set("")
        self._var_extra.set("")

    # ── Tab: Editar / Eliminar ─────────────────────────────────────────────

    def _construir_tab_editar(self):
        frame = self._tab_editar
        contenedor = tk.Frame(frame, bg=COLOR_PANEL, padx=30, pady=20)
        contenedor.pack(expand=True, padx=40, pady=30)

        tk.Label(contenedor, text="Editar o Eliminar Cliente",
                 font=FONT_SUBTITULO, bg=COLOR_PANEL, fg=COLOR_TEXTO
                 ).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 15))

        # Búsqueda por ID
        tk.Label(contenedor, text="ID del cliente", font=FONT_NORMAL,
                 bg=COLOR_PANEL, fg=COLOR_TEXTO_SUB).grid(row=1, column=0, sticky="w", pady=4)
        self._var_edit_id = tk.StringVar()
        tk.Entry(contenedor, textvariable=self._var_edit_id, font=FONT_NORMAL, width=15,
                 bg=COLOR_ENTRADA, fg=COLOR_TEXTO, insertbackground=COLOR_TEXTO,
                 relief="flat").grid(row=1, column=1, padx=10, pady=4, sticky="w")
        tk.Button(contenedor, text="🔍 Buscar", font=FONT_NORMAL,
                  bg=COLOR_ACENTO2, fg="white", relief="flat", padx=8,
                  command=self._buscar_para_editar).grid(row=1, column=2, padx=5)

        # Campos editables
        campos_edit = [
            ("Nombre", "nombre"), ("Email", "email"),
            ("Teléfono", "telefono"), ("Dirección", "direccion"), ("Extra", "extra")
        ]
        self._vars_editar = {}
        for i, (label, key) in enumerate(campos_edit, start=2):
            tk.Label(contenedor, text=label, font=FONT_NORMAL,
                     bg=COLOR_PANEL, fg=COLOR_TEXTO_SUB).grid(row=i, column=0, sticky="w", pady=4)
            var = tk.StringVar()
            self._vars_editar[key] = var
            tk.Entry(contenedor, textvariable=var, font=FONT_NORMAL, width=32,
                     bg=COLOR_ENTRADA, fg=COLOR_TEXTO, insertbackground=COLOR_TEXTO,
                     relief="flat", state="disabled").grid(row=i, column=1, columnspan=2,
                                                            padx=10, pady=4, sticky="w")

        self._entries_editar = {}  # Guardamos referencia para habilitar/deshabilitar

        # Botones
        btn_frame = tk.Frame(contenedor, bg=COLOR_PANEL)
        btn_frame.grid(row=len(campos_edit) + 2, column=0, columnspan=3, pady=20)

        self._btn_guardar_edicion = tk.Button(
            btn_frame, text="💾 Guardar cambios", font=FONT_NORMAL,
            bg=COLOR_EXITO, fg="white", relief="flat", padx=12, pady=6,
            command=self._guardar_edicion, state="disabled"
        )
        self._btn_guardar_edicion.pack(side="left", padx=8)

        self._btn_eliminar = tk.Button(
            btn_frame, text="🗑️ Eliminar cliente", font=FONT_NORMAL,
            bg=COLOR_ERROR, fg="white", relief="flat", padx=12, pady=6,
            command=self._eliminar_cliente, state="disabled"
        )
        self._btn_eliminar.pack(side="left", padx=8)

        self._lbl_tipo_edit = tk.Label(contenedor, text="", font=FONT_SMALL,
                                       bg=COLOR_PANEL, fg=COLOR_ACENTO2)
        self._lbl_tipo_edit.grid(row=len(campos_edit) + 3, column=0, columnspan=3)

        # Guardar referencias a los Entry widgets
        for widget in contenedor.winfo_children():
            if isinstance(widget, tk.Entry):
                pass  # Se reconstruirá de otra forma

        self._rebuild_edit_entries(contenedor, campos_edit)

    def _rebuild_edit_entries(self, contenedor, campos_edit):
        """Reconstruye los Entry con referencias para poder habilitarlos."""
        self._edit_entries = {}
        for i, (label, key) in enumerate(campos_edit, start=2):
            # Destruir Entry previo si existe
            for widget in contenedor.grid_slaves(row=i, column=1):
                widget.destroy()
            var = self._vars_editar[key]
            entry = tk.Entry(contenedor, textvariable=var, font=FONT_NORMAL, width=32,
                             bg=COLOR_ENTRADA, fg=COLOR_TEXTO, insertbackground=COLOR_TEXTO,
                             relief="flat", state="disabled")
            entry.grid(row=i, column=1, columnspan=2, padx=10, pady=4, sticky="w")
            self._edit_entries[key] = entry

    def _buscar_para_editar(self):
        """Carga los datos de un cliente en el formulario de edición."""
        try:
            cid_str = self._var_edit_id.get().strip()
            if not cid_str.isdigit():
                raise ValueError("Ingresá un ID numérico válido.")
            cid = int(cid_str)
            cliente = self.gestor.buscar(cid)

            # Poblar campos
            self._vars_editar["nombre"].set(cliente.get_nombre())
            self._vars_editar["email"].set(cliente.get_email())
            self._vars_editar["telefono"].set(cliente.get_telefono())
            self._vars_editar["direccion"].set(cliente.get_direccion())

            # Campo extra según tipo
            from tipos_cliente import ClienteRegular, ClientePremium, ClienteCorporativo
            if isinstance(cliente, ClienteRegular):
                self._vars_editar["extra"].set(str(cliente.get_puntos()))
                self._lbl_tipo_edit.config(text=f"Tipo: Regular | Campo extra: Puntos")
            elif isinstance(cliente, ClientePremium):
                self._vars_editar["extra"].set("")
                self._lbl_tipo_edit.config(text="Tipo: Premium | Campo extra: Nuevo beneficio")
            elif isinstance(cliente, ClienteCorporativo):
                self._vars_editar["extra"].set(cliente.get_empresa())
                self._lbl_tipo_edit.config(text="Tipo: Corporativo | Campo extra: Empresa")

            # Habilitar entries y botones
            for entry in self._edit_entries.values():
                entry.config(state="normal")
            self._btn_guardar_edicion.config(state="normal")
            self._btn_eliminar.config(state="normal")
            self._mostrar_estado(f"Cliente ID={cid} cargado para edición.", COLOR_ACENTO2)

        except ClienteNoEncontradoError as e:
            messagebox.showerror("No encontrado", str(e))
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def _guardar_edicion(self):
        """Guarda los cambios del formulario de edición."""
        try:
            cid = int(self._var_edit_id.get().strip())
            cliente = self.gestor.buscar(cid)

            kwargs = {
                "nombre":    self._vars_editar["nombre"].get(),
                "email":     self._vars_editar["email"].get(),
                "telefono":  self._vars_editar["telefono"].get(),
                "direccion": self._vars_editar["direccion"].get(),
            }

            from tipos_cliente import ClienteRegular, ClientePremium, ClienteCorporativo
            extra = self._vars_editar["extra"].get().strip()
            if isinstance(cliente, ClienteRegular) and extra.isdigit():
                kwargs["puntos"] = int(extra)
            elif isinstance(cliente, ClientePremium) and extra:
                kwargs["beneficio"] = extra
            elif isinstance(cliente, ClienteCorporativo) and extra:
                kwargs["empresa"] = extra

            self.gestor.editar(cid, **kwargs)
            self._mostrar_estado(f"✅ Cliente ID={cid} actualizado.", COLOR_EXITO)
            self._actualizar_tabla()

        except (ValidacionError, GICError) as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error inesperado", str(e))

    def _eliminar_cliente(self):
        """Elimina el cliente cargado en el formulario de edición."""
        try:
            cid = int(self._var_edit_id.get().strip())
            confirmar = messagebox.askyesno(
                "Confirmar eliminación",
                f"¿Estás seguro de que querés eliminar al cliente con ID {cid}?"
            )
            if not confirmar:
                return
            self.gestor.eliminar(cid)
            self._mostrar_estado(f"🗑️ Cliente ID={cid} eliminado.", COLOR_WARNING)
            self._actualizar_tabla()
            # Limpiar formulario
            for var in self._vars_editar.values():
                var.set("")
            for entry in self._edit_entries.values():
                entry.config(state="disabled")
            self._btn_guardar_edicion.config(state="disabled")
            self._btn_eliminar.config(state="disabled")
            self._var_edit_id.set("")
            self._lbl_tipo_edit.config(text="")

        except (ClienteNoEncontradoError, GICError) as e:
            messagebox.showerror("Error", str(e))

    # ── Tab: Exportar / Importar ───────────────────────────────────────────

    def _construir_tab_exportar(self):
        frame = self._tab_exportar
        contenedor = tk.Frame(frame, bg=COLOR_PANEL, padx=40, pady=30)
        contenedor.pack(expand=True)

        tk.Label(contenedor, text="Exportar / Importar Datos",
                 font=FONT_SUBTITULO, bg=COLOR_PANEL, fg=COLOR_TEXTO
                 ).pack(anchor="w", pady=(0, 20))

        def btn(texto, cmd, color):
            tk.Button(contenedor, text=texto, font=FONT_NORMAL, bg=color,
                      fg="white", relief="flat", padx=15, pady=8,
                      width=30, command=cmd).pack(pady=6)

        btn("📤 Exportar a JSON", self._exportar_json, COLOR_ACENTO)
        btn("📥 Importar desde JSON", self._importar_json, COLOR_ACENTO2)
        btn("📊 Exportar a CSV", self._exportar_csv, COLOR_REGULAR)
        btn("📂 Importar desde CSV", self._importar_csv, COLOR_CORP)

        self._lbl_export_resultado = tk.Label(contenedor, text="", font=FONT_NORMAL,
                                              bg=COLOR_PANEL, fg=COLOR_EXITO)
        self._lbl_export_resultado.pack(pady=15)

    def _exportar_json(self):
        ruta = filedialog.asksaveasfilename(
            defaultextension=".json", filetypes=[("JSON", "*.json")],
            initialfile="clientes.json"
        )
        if ruta:
            try:
                self.gestor.exportar_json(ruta)
                self._lbl_export_resultado.config(
                    text=f"✅ JSON exportado: {ruta}", fg=COLOR_EXITO)
            except GICError as e:
                messagebox.showerror("Error", str(e))

    def _importar_json(self):
        ruta = filedialog.askopenfilename(filetypes=[("JSON", "*.json")])
        if ruta:
            try:
                n = self.gestor.importar_json(ruta)
                self._actualizar_tabla()
                self._lbl_export_resultado.config(
                    text=f"✅ {n} clientes importados desde JSON.", fg=COLOR_EXITO)
            except GICError as e:
                messagebox.showerror("Error", str(e))

    def _exportar_csv(self):
        ruta = filedialog.asksaveasfilename(
            defaultextension=".csv", filetypes=[("CSV", "*.csv")],
            initialfile="clientes.csv"
        )
        if ruta:
            try:
                self.gestor.exportar_csv(ruta)
                self._lbl_export_resultado.config(
                    text=f"✅ CSV exportado: {ruta}", fg=COLOR_EXITO)
            except GICError as e:
                messagebox.showerror("Error", str(e))

    def _importar_csv(self):
        ruta = filedialog.askopenfilename(filetypes=[("CSV", "*.csv")])
        if ruta:
            try:
                n = self.gestor.importar_csv(ruta)
                self._actualizar_tabla()
                self._lbl_export_resultado.config(
                    text=f"✅ {n} clientes importados desde CSV.", fg=COLOR_EXITO)
            except GICError as e:
                messagebox.showerror("Error", str(e))

    # ── Helpers ────────────────────────────────────────────────────────────

    def _actualizar_tabla(self):
        """Recarga la tabla con todos los clientes del gestor."""
        for item in self._tabla.get_children():
            self._tabla.delete(item)

        clientes = self.gestor.listar()
        for c in clientes:
            self._tabla.insert("", "end", values=(
                c.get_id(),
                c.get_tipo(),
                c.get_nombre(),
                c.get_email(),
                c.get_telefono() or "—",
                f"{c.calcular_descuento():.1f}%",
                c.info_extra()
            ), tags=(c.get_tipo(),))

        self._lbl_contador.config(text=f"Total: {len(clientes)} clientes")

    def _filtrar_tabla(self):
        """Filtra la tabla según el texto de búsqueda."""
        texto = self._var_busqueda.get().lower()
        for item in self._tabla.get_children():
            self._tabla.delete(item)

        for c in self.gestor.listar():
            if (texto in str(c.get_id()) or
                texto in c.get_nombre().lower() or
                texto in c.get_email().lower() or
                texto in c.get_tipo().lower()):
                self._tabla.insert("", "end", values=(
                    c.get_id(), c.get_tipo(), c.get_nombre(), c.get_email(),
                    c.get_telefono() or "—",
                    f"{c.calcular_descuento():.1f}%", c.info_extra()
                ), tags=(c.get_tipo(),))

    def _mostrar_estado(self, mensaje, color=COLOR_EXITO):
        """Muestra un mensaje temporal en el header."""
        self._lbl_estado.config(text=mensaje, fg=color)
        self.after(4000, lambda: self._lbl_estado.config(text=""))


def iniciar_gui():
    """Punto de entrada para lanzar la GUI."""
    app = AplicacionGIC()
    app.mainloop()