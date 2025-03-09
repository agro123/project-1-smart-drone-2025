# project-1-smart-drone-2025

**Descripción:**
Primer proyecto para I.A. 2025
Se tiene un dron que debe recoger paquetes en un ambiente representado por
una matriz de 10x10. En cada búsqueda, el dron puede realizar movimientos simples tales como
desplazarse arriba, abajo, izquierda, y derecha. Cada movimiento cuesta 1. En el ambiente hay
casillas con campos electromagnéticos que afectan al dron. Si el dron llega a una casilla con campo
electromagnético, le cuesta 8. Este costo ya tiene incluido el valor del desplazamiento. Usted debe
utilizar algoritmos de búsqueda para determinar el recorrido del dron. La cantidad de paquetes a
recoger y el número de casillas con campo electromagnético puede variar de un ambiente a otro.
Cuando el dron llega a una casilla donde hay un paquete, lo toma automáticamente. La búsqueda
termina cuando se recojan todos los paquetes del ambiente.

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