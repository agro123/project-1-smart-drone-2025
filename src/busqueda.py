from algoritmos.amplitud import amplitud
from algoritmos.costo_uniforme import costo_uniforme
from algoritmos.avara import avara
from algoritmos.a_star import a_star
from algoritmos.profundidad import profundidad
from helpers import SearchType
import time

#tipo_busqueda, matriz => nodo_final, nodos_expandidoss (por definir su estructura)
def busqueda(search_type, matriz):
    initial_pos = (0,0) # [fila,columna]: posicion del valor 2 en la matriz
    goalsPos = [] #Lista de posiciones de los valores 4 en la matriz
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == 2:
                initial_pos = (i, j)
            elif matriz[i][j] == 4:
                goalsPos.append((i, j))

    print(f"Posición inicial Dron: ({initial_pos[0]}, {initial_pos[1]})")
    print(f"Número de paquetes por recoger: {len(goalsPos)}")
    nodo_final = None
    nodos_expandidos = None
    inicio = time.time() * 1000 
    if SearchType(search_type) == SearchType.AMPLITUD:
        nodo_final, nodos_expandidos = amplitud(matriz, initial_pos, goalsPos)
    if SearchType(search_type) == SearchType.COSTO_UNIFORME:
        nodo_final, nodos_expandidos = costo_uniforme(matriz, initial_pos, goalsPos)
    if SearchType(search_type) == SearchType.AVARA:
        nodo_final, nodos_expandidos = avara(matriz, initial_pos, goalsPos)
    if SearchType(search_type) == SearchType.A_START:
        nodo_final, nodos_expandidos = a_star(matriz, initial_pos, goalsPos)
    if SearchType(search_type) == SearchType.PROFUNDIDAD:
        nodo_final, nodos_expandidos = profundidad(matriz, initial_pos, goalsPos)
    fin = time.time() * 1000 

    tiempo_ejecucion = fin - inicio

    
    
    return [nodo_final, nodos_expandidos, tiempo_ejecucion]


exampleValue = [[1, 1, 0, 0, 0, 0, 0, 1, 1, 1], [1, 1, 0, 1, 0, 1, 0, 1, 1, 1], [0, 2, 0, 3, 4, 4, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 0, 0, 0, 0, 0, 0], [3, 3, 0, 1, 0, 1, 1, 1, 1, 1], [1, 1, 0, 1, 0, 0, 0, 0, 0, 0], [1, 1, 0, 1, 1, 1, 1, 1, 1, 0], [1, 1, 0, 0, 0, 0, 4, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
busqueda(SearchType.A_START, exampleValue)