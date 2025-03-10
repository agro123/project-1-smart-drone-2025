from mapa import MAP_SIZE 

def get_cell_cost(value):
    if value == 3:
        return 8
    else:
        return 1
    
class Nodo:
    def __init__(self, pos=None, padre=None, operador=None, profundidad=0, costo=0, cajas_obtenidas = 0):
        self.padre = padre
        self.operador = operador
        self.profundidad = profundidad
        self.costo = costo
        self.cajas_obtenidas = cajas_obtenidas
        self.pos = pos

    #Verificar el costo de ir a algun lado
    def ir_izquierda(self, matriz):
        columna = self.pos[1] - 1
        #Verificar que no supere las dimensiones de la matriz
        if columna < 0:
            return {"valor": 1}

        return {
            "valor": matriz[self.pos[0]][columna],
            "n_pos": [self.pos[0], columna],
            "costo": get_cell_cost(matriz[self.pos[0]][columna])
        }
    
    def ir_arriba(self, matriz):
        fila = self.pos[0] - 1
        if fila < 0:
            return {"valor": 1}

        return {
            "valor": matriz[fila][self.pos[1]],
            "n_pos": [fila, self.pos[1]],
            "costo": get_cell_cost(matriz[fila][self.pos[1]])
        }

    def ir_derecha(self, matriz):
        columna = self.pos[1] + 1
        if columna > MAP_SIZE - 1:
            return {"valor": 1}

        return {
            "valor": matriz[self.pos[0]][columna],
            "n_pos": [self.pos[0], columna],
            "costo": get_cell_cost(matriz[self.pos[0]][columna])
        }

    def ir_abajo(self, matriz):
        fila = self.pos[0] + 1
        if fila > MAP_SIZE - 1:
            return {"valor": 1}
        return {
            "valor": matriz[fila][self.pos[1]],
            "n_pos": [fila, self.pos[1]],
            "costo": get_cell_cost(matriz[fila][self.pos[1]])
        }
    
    def verificar_caja(self, matriz):
        if  matriz[self.pos[0]][self.pos[1]] == 4:
            self.cajas_obtenidas = self.cajas_obtenidas + 1
        return self.cajas_obtenidas

    def es_estado_repetido(self):
        #Para evitar devolverse
        nodo_actual = self.padre
        #while nodo_actual:
        if nodo_actual.pos == self.pos:
            return True  # Ya visitamos esta posición
            #nodo_actual = nodo_actual.padre
        return False

    def mostrar_profundidad(self):
        print(f"La profundidad del nodo es {self.profundidad}")
    
    def mostrar_operador(self):
        print(f"El operador usado para llegar a este nodo fue {self.operador}")