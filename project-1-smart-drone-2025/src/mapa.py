import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

MAP_SIZE = 10

class InterfazDronGUI:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Dron Inteligente")
        self.ventana.configure(bg='#2C3E50')

        self.archivo_mapa = None
        self.map = [[0 for _ in range(MAP_SIZE)] for _ in range(MAP_SIZE)] #matriz por defecto
        self.imagenes = {}  # Diccionario para almacenar imágenes
        self.portada_mostrada = True

        self.mostrar_portada()
        self.ventana.mainloop()

    def mostrar_portada(self):
        """Muestra la imagen de portada con el botón de iniciar"""
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
        """Oculta la portada y muestra la interfaz principal"""
        self.frame_portada.pack_forget()
        self.crear_interfaz_principal()

    def crear_interfaz_principal(self):
        """Crea la interfaz del juego"""
        self.ventana.geometry("700x600")

        self.frame_cuadricula = tk.Frame(self.ventana, bg='#34495E')
        self.frame_cuadricula.pack(pady=20)

        self.canvas = tk.Canvas(self.frame_cuadricula, width=500, height=500, bg='#ECF0F1')
        self.canvas.pack()

        self.boton_cargar = tk.Button(
            self.ventana,
            text="Cargar Mapa",
            font=("Arial", 14, "bold"),
            bg='#E74C3C',
            fg='white',
            width=15,
            command=self.cargar_archivo
        )
        self.boton_cargar.pack(pady=10)

        self.cargar_imagenes()

    def cargar_imagenes(self):
        """Carga las imágenes de los íconos en un diccionario"""
        ruta_assets = "assets"

        self.imagenes = {
            2: ImageTk.PhotoImage(Image.open(os.path.join(ruta_assets, "dron.png")).resize((50, 50), Image.LANCZOS)),
            3: ImageTk.PhotoImage(Image.open(os.path.join(ruta_assets, "campo.png")).resize((50, 50), Image.LANCZOS)),
            4: ImageTk.PhotoImage(Image.open(os.path.join(ruta_assets, "paquete.png")).resize((50, 50), Image.LANCZOS))
        }

    def cargar_archivo(self):
        """Carga un archivo de mapa y lo dibuja"""
        archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
        if archivo:
            self.archivo_mapa = archivo
            messagebox.showinfo("Mapa Cargado", "Mapa cargado correctamente.")
            self.ventana.geometry("700x700")
            self.dibujar_mapa()

    def dibujar_mapa(self):
        """Dibuja la cuadrícula del mapa con imágenes y colores"""
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

    def start (self): 
        if not self.map:
            return None
        #todo



