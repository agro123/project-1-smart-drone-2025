import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import os
from busqueda import busqueda
import copy
from collections import deque
import pygame
import os

MAP_SIZE = 10

class InterfazDronGUI:
    def __init__(self):

   # Inicializar Pygame Mixer para sonidos
        pygame.mixer.init()

          # canal para otros efectos

        self.sonidos = {
           "inicio": pygame.mixer.Sound("assets/sounds/inicio.wav"),
           "boton": pygame.mixer.Sound("assets/sounds/boton.wav"),
           "campo": pygame.mixer.Sound("assets/sounds/campo.wav"),
            "caja": pygame.mixer.Sound("assets/sounds/caja.wav"),
            "buscar": pygame.mixer.Sound("assets/sounds/buscar.wav"),
            "cargar": pygame.mixer.Sound("assets/sounds/cargar.wav"),
             "reiniciar": pygame.mixer.Sound("assets/sounds/reiniciar.wav"),
             
           
            
        }
         # Reproducir sonido de inicio
        self.sonidos["inicio"].play()


        # Configuración de la ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("Dron Inteligente")
        self.ventana.configure(bg='#2C3E50')



        self.archivo_mapa = None
        self.map = [[0 for _ in range(MAP_SIZE)] for _ in range(MAP_SIZE)]  # Matriz por defecto
        self.imagenes = {}  # Diccionario para almacenar imágenes
        self.portada_mostrada = True
        self.mapa_original = None  # Aquí guardaremos una copia del mapa original


        self.mostrar_portada()
        self.centrar_ventana()  # Centrar la ventana al iniciar
        self.ventana.mainloop()

    def centrar_ventana(self):
        """Centra la ventana en la pantalla"""
        self.ventana.update_idletasks()  # Actualiza las dimensiones de la ventana
        ancho_ventana = self.ventana.winfo_width()
        alto_ventana = self.ventana.winfo_height()
        ancho_pantalla = self.ventana.winfo_screenwidth()
        alto_pantalla = self.ventana.winfo_screenheight()

        x = (ancho_pantalla // 2) - (ancho_ventana // 2)
        y = (alto_pantalla // 2) - (alto_ventana // 2)

        self.ventana.geometry(f"+{x}+{y}")

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
        self.sonidos["inicio"].stop()
           # Reproducir el sonido del botón al presionar el botón
        self.sonidos["boton"].play()
        self.frame_portada.pack_forget()
        self.crear_interfaz_principal()
        self.centrar_ventana()  # Centrar la ventana después de iniciar el juego

    def crear_interfaz_principal(self):
        """Crea la interfaz del juego"""
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

        self.boton_reiniciar = tk.Button(
            self.frame_botones,
            text="Reiniciar",
            font=("Arial", 14, "bold"),
            bg='#2ECC71',
            fg='white',
            width=15,
            command=self.reiniciar_mapa
        )
        self.boton_reiniciar.pack(side=tk.LEFT, padx=10)

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

        self.frame_info = tk.Frame(self.ventana, bg='#2C3E50')
        self.frame_info.pack(fill='x', pady=10)
        self.label_costo = tk.Label(
            self.frame_info,
            text="Costo: N/A",
            bg='#2C3E50',
            fg='white',
            font=("Arial", 12)
        )
        self.label_costo.pack(side=tk.LEFT, padx=20)

        self.label_profundidad = tk.Label(
            self.frame_info,
            text="Profundidad árbol: N/A",
            bg='#2C3E50',
            fg='white',
            font=("Arial", 12)
        )
        self.label_profundidad.pack(side=tk.LEFT, padx=20)

        self.label_nodos_expandidos = tk.Label(
            self.frame_info,
            text="Nodos expandidos: N/A",
            bg='#2C3E50',
            fg='white',
            font=("Arial", 12)
        )
        self.label_nodos_expandidos.pack(side=tk.LEFT, padx=20)

        self.label_tiempo_computo = tk.Label(
            self.frame_info,
            text="Tiempo de cómputo: N/A",
            bg='#2C3E50',
            fg='white',
            font=("Arial", 12)
        )
        self.label_tiempo_computo.pack(side=tk.LEFT, padx=20)

        self.cargar_imagenes()

    def reiniciar_mapa(self):
     self.sonidos["reiniciar"].play()
     """Recarga el mapa original y reinicia todos los datos"""
     if not self.archivo_mapa:
        messagebox.showerror("Error", "No hay mapa cargado para reiniciar.")
        return
    
    # Cancelar cualquier animación pendiente
     if hasattr(self, '_after_id'):
        self.ventana.after_cancel(self._after_id)
        del self._after_id
    
    # Reiniciar métricas
     self.label_costo.config(text="Costo: N/A")
     self.label_profundidad.config(text="Profundidad: N/A")
     self.label_nodos_expandidos.config(text="Nodos expandidos: N/A")
     self.label_tiempo_computo.config(text="Tiempo de cómputo: N/A")
    
    # Reiniciar selecciones pero manteniendo habilitados los combobox
     self.tipo_busqueda.set("seleccione")
     self.algoritmo.set("seleccione")
     self.menu_algoritmo.config(values=["Búsqueda no informada - evitando ciclos"])
     self.menu_algoritmo.config(state="readonly")  # Cambiado de DISABLED a readonly
    
    # Restaurar mapa original
     if self.mapa_original:
        self.map = copy.deepcopy(self.mapa_original)
        self.dibujar_mapa()
    
    # No deshabilitar el botón de buscar, solo resetear estado
     self.boton_buscar.config(state=tk.NORMAL if self.archivo_mapa else tk.DISABLED)

    def actualizar_algoritmos(self, event):
        tipo_busqueda = self.tipo_busqueda.get()
        if tipo_busqueda == "No informada":
            opciones = ["Amplitud", "Costo uniforme", "Profundidad evitando ciclos"]
        elif tipo_busqueda == "Informada":
            opciones = ["Avara", "A*"]
        else:
            opciones = []

        self.menu_algoritmo.config(values=opciones)
        self.menu_algoritmo.set(opciones[0] if opciones else "")
        self.menu_algoritmo.config(state="readonly")  # Siempre readonly en lugar de DISABLED

    def cargar_imagenes(self):
        """Carga las imágenes de los íconos en un diccionario"""
        ruta_assets = "assets"

        self.imagenes = {
            2: ImageTk.PhotoImage(Image.open(os.path.join(ruta_assets, "dron.png")).resize((50, 50), Image.LANCZOS)),
            3: ImageTk.PhotoImage(Image.open(os.path.join(ruta_assets, "campo.png")).resize((50, 50), Image.LANCZOS)),
            4: ImageTk.PhotoImage(Image.open(os.path.join(ruta_assets, "paquete.png")).resize((50, 50), Image.LANCZOS))
        }

    def cargar_archivo(self):
        self.sonidos["cargar"].play()
        """Carga un archivo de mapa y lo dibuja"""
        archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
        if archivo:
            self.archivo_mapa = archivo
            with open(self.archivo_mapa , "r") as file:
               self.mapa_original = [list(map(int, line.split())) for line in file] # Guardar una copia del mapa original

            messagebox.showinfo("Mapa Cargado", "Mapa cargado correctamente.")
            self.ventana.geometry("700x700")
            self.dibujar_mapa()
            self.boton_buscar.config(state=tk.NORMAL)

    def dibujar_mapa(self):
        """Dibuja la cuadrícula del mapa con imágenes y colores"""
        if not self.archivo_mapa:
            return
        
        with open(self.archivo_mapa, "r") as file:
            matriz = [list(map(int, line.split())) for line in file]
        self.canvas.delete("all")

        self.map = matriz
        for i, fila in enumerate(matriz):
            for j, valor in enumerate(fila):
                self.dibujar_celda(i, j)

    def dibujar_celda(self, i, j, matriz=None):
            tam_celda = 50
            x1, y1 = j * tam_celda, i * tam_celda
            x2, y2 = x1 + tam_celda, y1 + tam_celda
            valor = None
            if matriz:
                valor = matriz[i][j]
            else:
                valor = self.map[i][j]
            # Colores de fondo
            colores = {0: '#BDC3C7', 1: '#7F8C8D', 5: '#F1C40F'} # Libre y obstáculos
            color = colores.get(valor, 'white')
            # Dibuja el fondo de la celda
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline='#34495E')
            # Si hay un ícono (dron, paquete, campo electromagnético), lo dibuja
            if valor in self.imagenes:
                self.canvas.create_image(x1 + 25, y1 + 25, image=self.imagenes[valor])

    def ejecutar_busqueda(self):
        self.sonidos["buscar"].play()  # <<< sonido al presionar
        if not self.archivo_mapa:
            messagebox.showerror("Error", "No se ha cargado ningún mapa.")
            return

        tipo_busqueda = self.tipo_busqueda.get()
        algoritmo = self.algoritmo.get()

      # Evita múltiples ejecuciones simultáneas
        after_id = getattr(self, '_after_id', None)
        if after_id is not None:
         self.ventana.after_cancel(after_id)
         self._after_id = None
                 
        # Restaurar el mapa original antes de ejecutar la búsqueda
        if self.mapa_original:
         self.map = copy.deepcopy(self.mapa_original)
         self.dibujar_mapa()


        if algoritmo == "seleccione" or not algoritmo:
         messagebox.showerror("Error", "Seleccione un algoritmo de búsqueda válido.")
         return

        if tipo_busqueda == "seleccione" or not tipo_busqueda:
         messagebox.showerror("Error", "Seleccione un tipo de búsqueda válido.")
         return


        if algoritmo and tipo_busqueda:
            result = busqueda(algoritmo, self.map)
            messagebox.showinfo("Búsqueda", f"Ejecutando búsqueda {tipo_busqueda} con {algoritmo}...")
        else:
            messagebox.showerror("Error", "Seleccione un algoritmo de búsqueda.")

        if result[0] :
            nodo_final, nodos_expandidos, tiempo_ejecucion, profundiad_arbol = result
            #result es tipo [nodo, nodos_expandidos, tiempo_ejecucion]
            self.label_costo.config(text=f"Costo: {nodo_final.costo}")
            self.label_profundidad.config(text=f"Profundidad árbol: {profundiad_arbol}")
            self.label_nodos_expandidos.config(text=f"Nodos expandidos: {nodos_expandidos}")
            self.label_tiempo_computo.config(text=f"Tiempo de cómputo: {tiempo_ejecucion} ms")

            self.ejecutar_animacion(nodo_final)
        else:
            messagebox.showerror("Error", "Ocurrio un error en la búsqueda.")

    def ejecutar_animacion(self, nodo_final):
        matriz = copy.deepcopy(self.map)
        camino = deque(nodo_final.trayectoria())  # Obtener el camino desde el nodo final
        if not camino:
            return
        
    # Limpiar cualquier dron en la matriz antes de iniciar la animación
        for i in range(len(matriz)):
         for j in range(len(matriz[0])):
          if  matriz[i][j] == 2:
             matriz[i][j] = 5
             self.dibujar_celda(i, j, matriz)

        dron_actual = None
        
        i_inicio, j_inicio = camino[0]
        if matriz[i_inicio][j_inicio] == 2:
            matriz[i_inicio][j_inicio] = 5  # O el valor que uses para "camino libre"
            self.dibujar_celda(i_inicio, j_inicio, matriz)
                 # Guarda la posición anterior del dron
        

        def mover():
            nonlocal dron_actual
            if not camino:
                return

            i, j = camino.popleft()

            # Borrar el dron anterior (volverlo 0 en matriz y redibujar)
            if dron_actual:
                x_old, y_old = dron_actual
                matriz[x_old][y_old] = 5
                self.dibujar_celda(x_old, y_old, matriz)

                # Reproducir sonido si entra en un campo electromagnético
            if matriz[i][j] == 3:
                self.sonidos["campo"].play()

            
            # Si hay un paquete, lo recoge (cambia a 0)
            if matriz[i][j] == 4:
                self.sonidos["caja"].play()
                matriz[i][j] = 0  # Lo cambia a camino antes de poner el dron


            # Poner el dron en la nueva posición
            matriz[i][j] = 2
            
            self.dibujar_celda(i, j, matriz)

            # Guardar la posición actual como anterior para el próximo paso
            dron_actual = (i, j)

          # Verificar si quedan cajas (valor 4) en el mapa
            cajas_restantes = any(4 in fila for fila in matriz)
            if not cajas_restantes and not camino:  # Si no quedan cajas y terminó el camino
                messagebox.showinfo("Búsqueda finalizada", "¡El dron ha recogido todas las cajas!")
                return   

            self._after_id = self.ventana.after(300, mover)
        mover()


    def start(self): 
        if not self.map:
            return None
        #todo