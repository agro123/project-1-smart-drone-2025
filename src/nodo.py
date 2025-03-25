from helpers import MAP_SIZE
from enum import Enum
from typing import List
import copy

class Movement(Enum):
    LEFT = 1
    TOP = 2
    RIGHT = 3
    DOWN = 4

def get_cell_cost(value):
    if value == 3:
        return 8
    else:
        return 1
    
#Retorna la menor distancia de manhattan entre una posición y los objetivos
def menor_distancia_manhattan(currPos, objetivos):
    if len(objetivos) == 0:
        return 0
    return min(abs(currPos[0] - obj[0]) + abs(currPos[1] - obj[1]) for obj in objetivos)
    
class Nodo:
    def __init__(self, pos=(0,0), padre=None, operador=None, profundidad=0, costo=0, posicion_objetivos = []):
        self.padre = padre
        self.operador = operador
        self.profundidad = profundidad
        self.costo = costo #costo acumulado
        self.pos = pos
        self.posicion_objetivos = copy.deepcopy(posicion_objetivos)
        self.h = menor_distancia_manhattan(pos, self.posicion_objetivos)
        self.hg = self.h + self.costo

    def ir(self, matriz: List[List[int]], movement: Movement):
        fila = self.pos[0]
        columna = self.pos[1]
        if(movement == Movement.LEFT):
            columna = columna - 1
        elif(movement == Movement.TOP):
            fila = fila - 1
        elif(movement == Movement.RIGHT):
            columna = columna + 1
        elif(movement == Movement.DOWN):
            fila = fila + 1
        #Verificar que no supere las dimensiones de la matriz
        if fila < 0 or columna < 0 or columna > MAP_SIZE - 1 or fila > MAP_SIZE - 1:
            return {"valor": 1}

        return {
            "valor": matriz[fila][columna],
            "n_pos": (fila, columna),
            "costo": get_cell_cost(matriz[fila][columna]),
            "operador": movement
        }

    def verificar_caja(self):
        if  self.pos in self.posicion_objetivos:
            self.posicion_objetivos.remove(self.pos)
        
        return len(self.posicion_objetivos)

    def evitar_ciclos(self):
        #Para evitar ciclos
        padre = self.padre
        while padre:
            if padre.pos == self.pos:
                return True
            padre = padre.padre
        return False

    def no_devolverse(self):
        #Para evitar devolverse
        return self.padre.pos == self.pos

    def mostrar_profundidad(self):
        print(f"La profundidad del nodo es {self.profundidad}")
    
    def mostrar_operador(self):
        print(f"El operador usado para llegar a este nodo fue {self.operador}")

    def mostrar_costo(self):
        print(f"El costo fue {self.costo}")

    def trayectoria(self):
        resultado = []
        nodo_actual = self

        while nodo_actual:
            if nodo_actual.operador is not None:  # Evitar agregar operador de nodo raíz
                resultado.append(nodo_actual.operador)
            nodo_actual = nodo_actual.padre

        resultado.reverse()  # Invertimos la trayectoria para que sea del inicio al final
        print('Trayectoria:', resultado)
        return resultado
