import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import os
from algoritmos.amplitud import amplitud
MAP_SIZE = 10  # Tamaño del mapa

class InterfazDronGUI:
    def __init__(self):
        """
        Inicializa la interfaz gráfica del dron.
        """
        self.ventana = tk.Tk()
        self.ventana.title("Dron Inteligente")
        self.ventana.configure(bg='#2C3E50')

        self.archivo_mapa = None  # Archivo de mapa cargado
        self.map = [[0 for _ in range(MAP_SIZE)] for _ in range(MAP_SIZE)]  # Matriz del mapa
        self.imagenes = {}  # Diccionario para almacenar imágenes
        self.portada_mostrada = True  # Estado de la portada

        self.mostrar_portada()  # Mostrar la portada inicial
        self.centrar_ventana()  # Centrar la ventana en la pantalla
        self.ventana.mainloop()

    def centrar_ventana(self):
        """
        Centra la ventana en la pantalla.
        """
        self.ventana.update_idletasks()
        ancho_ventana = self.ventana.winfo_width()
        alto_ventana = self.ventana.winfo_height()
        ancho_pantalla = self.ventana.winfo_screenwidth()
        alto_pantalla = self.ventana.winfo_screenheight()

        x = (ancho_pantalla // 2) - (ancho_ventana // 2)
        y = (alto_pantalla // 2) - (alto_ventana // 2)

        self.ventana.geometry(f"+{x}+{y}")

    def mostrar_portada(self):
        """
        Muestra la imagen de portada con el botón de iniciar.
        """
        self.frame_portada = tk.Frame(self.ventana, bg="black")
        self.frame_portada.pack(fill="both", expand=True)

        ruta_imagen = "assets/portada.png"
        portada = Image.open(ruta_imagen).resize((700, 500), Image.LANCZOS)
        self.img_portada = ImageTk.PhotoImage(portada)

        self.ventana.geometry(f"{portada.width}x{portada.height}")

        self.label_portada = tk.Label(self.frame_portada, image=self.img_portada)
        self.label_portada.pack(fill="both", expand=True)

        self.boton_iniciar = tk.Button(
            self.frame_portada,
            text="Iniciar Juego",
            font=("Arial", 16, "bold"),
            bg="#E74C3C",
            fg="white",
            command=self.iniciar_programa
        )
        self.boton_iniciar.place(relx=0.5, rely=0.9, anchor="center")

    def iniciar_programa(self):
        """
        Oculta la portada y muestra la interfaz principal.
        """
        self.frame_portada.pack_forget()
        self.crear_interfaz_principal()
        self.centrar_ventana()

    def crear_interfaz_principal(self):
        """
        Crea la interfaz principal del juego.
        """
        self.ventana.geometry("700x700")

        self.frame_cuadricula = tk.Frame(self.ventana, bg='#34495E')
        self.frame_cuadricula.pack(pady=20)

        self.canvas = tk.Canvas(self.frame_cuadricula, width=500, height=500, bg='#ECF0F1')
        self.canvas.pack()

        self.frame_botones = tk.Frame(self.ventana, bg='#2C3E50')
        self.frame_botones.pack(fill='x', pady=10)

        self.boton_cargar = tk.Button(
            self.frame_botones,
            text="Cargar Mapa",
            font=("Arial", 14, "bold"),
            bg='#E74C3C',
            fg='white',
            width=15,
            command=self.cargar_archivo
        )
        self.boton_cargar.pack(side=tk.LEFT, padx=10)

        self.boton_buscar = tk.Button(
            self.frame_botones,
            text="Buscar y Recoger",
            font=("Arial", 14, "bold"),
            bg='#3498DB',
            fg='white',
            width=15,
            command=self.ejecutar_busqueda,
            state=tk.DISABLED
        )
        self.boton_buscar.pack(side=tk.LEFT, padx=10)

        self.frame_seleccion = tk.Frame(self.ventana, bg='#2C3E50')
        self.frame_seleccion.pack(fill='x', pady=10)

        self.label_tipo_busqueda = tk.Label(
            self.frame_seleccion,
            text="Seleccione tipo de búsqueda:",
            bg='#2C3E50',
            fg='white',
            font=("Arial", 12)
        )
        self.label_tipo_busqueda.pack(side=tk.LEFT, padx=10)

        self.tipo_busqueda = tk.StringVar(value="seleccione")
        self.menu_busqueda = ttk.Combobox(
            self.frame_seleccion,
            textvariable=self.tipo_busqueda,
            values=["No informada", "Informada"],
            state="readonly"
        )
        self.menu_busqueda.pack(side=tk.LEFT, padx=10)
        self.menu_busqueda.bind("<<ComboboxSelected>>", self.actualizar_algoritmos)

        self.label_algoritmo = tk.Label(
            self.frame_seleccion,
            text="Seleccione algoritmo:",
            bg='#2C3E50',
            fg='white',
            font=("Arial", 12)
        )
        self.label_algoritmo.pack(side=tk.LEFT, padx=10)

        self.algoritmo = tk.StringVar(value="seleccione")
        self.menu_algoritmo = ttk.Combobox(
            self.frame_seleccion,
            textvariable=self.algoritmo,
            values=["Búsqueda no informada - evitando ciclos"],
            state="readonly"
        )
        self.menu_algoritmo.pack(side=tk.LEFT, padx=10)

        self.cargar_imagenes()

    def actualizar_algoritmos(self, event):
        """
        Actualiza las opciones de algoritmos según el tipo de búsqueda seleccionado.
        """
        tipo_busqueda = self.tipo_busqueda.get()
        if tipo_busqueda == "No informada":
            opciones = ["Amplitud", "Costo uniforme", "Profundidad evitando ciclos"]
        elif tipo_busqueda == "Informada":
            opciones = ["Avara", "A*"]
        else:
            opciones = []

        self.menu_algoritmo.config(values=opciones)
        self.menu_algoritmo.set(opciones[0] if opciones else "")
        self.menu_algoritmo.config(state=tk.NORMAL if opciones else tk.DISABLED)

    def cargar_imagenes(self):
        """
        Carga las imágenes de los íconos en un diccionario.
        """
        ruta_assets = "assets"

        self.imagenes = {
            2: ImageTk.PhotoImage(Image.open(os.path.join(ruta_assets, "dron.png")).resize((50, 50), Image.LANCZOS)),
            3: ImageTk.PhotoImage(Image.open(os.path.join(ruta_assets, "campo.png")).resize((50, 50), Image.LANCZOS)),
            4: ImageTk.PhotoImage(Image.open(os.path.join(ruta_assets, "paquete.png")).resize((50, 50), Image.LANCZOS))
        }

    def cargar_archivo(self):
        """
        Carga un archivo de mapa y lo dibuja en la interfaz.
        """
        archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
        if archivo:
            self.archivo_mapa = archivo
            messagebox.showinfo("Mapa Cargado", "Mapa cargado correctamente.")
            self.ventana.geometry("700x700")
            self.dibujar_mapa()
            self.boton_buscar.config(state=tk.NORMAL)

    def dibujar_mapa(self):
        """
        Dibuja la cuadrícula del mapa con imágenes y colores.
        """
        if not self.archivo_mapa:
            return

        with open(self.archivo_mapa, "r") as file:
            matriz = [list(map(int, line.split())) for line in file]

        self.canvas.delete("all")
        tam_celda = 50

        # Colores de fondo
        colores = {0: '#BDC3C7', 1: '#7F8C8D'}  # Libre y obstáculos
        self.map = matriz
        for i, fila in enumerate(matriz):
            for j, valor in enumerate(fila):
                x1, y1 = j * tam_celda, i * tam_celda
                x2, y2 = x1 + tam_celda, y1 + tam_celda
                color = colores.get(valor, 'white')

                # Dibuja el fondo de la celda
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='#34495E')

                # Si hay un ícono (dron, paquete, campo electromagnético), lo dibuja
                if valor in self.imagenes:
                    self.canvas.create_image(x1 + 25, y1 + 25, image=self.imagenes[valor])

    def ejecutar_busqueda(self):
        """
        Ejecuta el algoritmo de búsqueda seleccionado y muestra la trayectoria.
        """
        if not self.archivo_mapa:
            messagebox.showerror("Error", "No se ha cargado ningún mapa.")
            return

        tipo_busqueda = self.tipo_busqueda.get()
        algoritmo = self.algoritmo.get()

        if tipo_busqueda == "No informada" and algoritmo == "Amplitud":
            messagebox.showinfo("Búsqueda", "Ejecutando búsqueda en amplitud...")

            # Cargar el mapa desde el archivo
            with open(self.archivo_mapa, "r") as file:
                matriz = [list(map(int, line.split())) for line in file]

            # Ejecutar el algoritmo de amplitud
            resultado = amplitud(matriz, pos=[0, 0], goals_number=1)

            if resultado:
                # Mostrar la trayectoria en el mapa
                self.mostrar_trayectoria(resultado.trayectoria())
            else:
                messagebox.showerror("Error", "No se encontró una solución.")
        elif tipo_busqueda == "No informada" and algoritmo == "Costo uniforme":
            messagebox.showinfo("Búsqueda", "Ejecutando búsqueda de costo uniforme...")
        elif tipo_busqueda == "No informada" and algoritmo == "Profundidad evitando ciclos":
            messagebox.showinfo("Búsqueda", "Ejecutando búsqueda en profundidad evitando ciclos...")
        elif tipo_busqueda == "Informada" and algoritmo == "Avara":
            messagebox.showinfo("Búsqueda", "Ejecutando búsqueda avara...")
        elif tipo_busqueda == "Informada" and algoritmo == "A*":
            messagebox.showinfo("Búsqueda", "Ejecutando búsqueda A*...")
        else:
            messagebox.showerror("Error", "Algoritmo no implementado o incorrecto.")

    def mostrar_trayectoria(self, trayectoria):
        """
        Muestra la trayectoria en el mapa.
        """
        tam_celda = 50

        for i, fila in enumerate(self.map):
            for j, valor in enumerate(fila):
                x1, y1 = j * tam_celda, i * tam_celda
                x2, y2 = x1 + tam_celda, y1 + tam_celda

                if (i, j) in trayectoria:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill='yellow', outline='#34495E')

        # Mover el dron a lo largo de la trayectoria
        self.mover_dron(trayectoria)

    def mover_dron(self, trayectoria, index=0):
        """
        Anima el movimiento del dron a lo largo de la trayectoria.
        """
        if index < len(trayectoria):
            fila, columna = trayectoria[index]
            x = columna * 50 + 25
            y = fila * 50 + 25

            # Mover el dron a la nueva posición
            self.canvas.delete("dron")  # Eliminar la imagen anterior del dron
            self.canvas.create_image(x, y, image=self.imagenes[2], tags="dron")

            # Llamar a la función nuevamente después de un tiempo
            self.ventana.after(500, lambda: self.mover_dron(trayectoria, index + 1))
        else:
            messagebox.showinfo("Búsqueda", "El dron ha llegado al destino.")