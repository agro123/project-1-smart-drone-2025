# 🚁 Project 1 – Smart Drone 2025

## 📘 Descripción ##

Primer proyecto  de Inteligencia Artificial (2025).  
Se ha desarrollado un simulador de dron inteligente capaz de recoger paquetes en un ambiente representado por una matriz de **10x10**.

El dron puede realizar movimientos simples (arriba, abajo, izquierda, derecha), cada uno con un **costo de 1**.  
En el entorno existen casillas con **campos electromagnéticos** que afectan al dron: si entra en una de ellas, el movimiento tiene un **costo total de 8** (ya incluye el movimiento).

El objetivo es recolectar todos los paquetes automáticamente mediante **algoritmos de búsqueda**, optimizando el recorrido según el costo del entorno.

### 🧠 Lógica del proyecto:### 

- El dron inicia con un mapa cargado.
- Busca automáticamente el camino óptimo para recoger los paquetes.
- La cantidad de paquetes y casillas peligrosas puede variar en cada mapa.
- Se usó el patrón de arquitectura **MVC** para organizar el código.
- Se integraron **efectos de sonido** para mejorar la experiencia visual y auditiva.

---

## 🔧 Tecnologías y Librerías Utilizadas

- **Python 3.x**
- **Tkinter** – para la interfaz gráfica (incluido con Python)
- **Pygame** – para reproducir efectos de sonido (`pip install pygame`)
- **OS**, **time**, **random** – módulos estándar

> Asegúrate de tener estas librerías instaladas antes de ejecutar el programa.
---
## ⚙️ Instalación y Ejecución

### 1. Clona el repositorio:
```bash
git clone https://github.com/tu-usuario/project-1-smart-drone-2025.git
cd project-1-smart-drone-2025


**Activar el entorno virtual:**
- **Windows**
    ```bash
       .\env\Scripts\activate

- **MacOS/Linux**
    ```bash
       source env/bin/activate

**Iniciar**
    ```bash
       python src/main.py