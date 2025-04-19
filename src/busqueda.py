from algoritmos.amplitud import amplitud
from algoritmos.costo_uniforme import costo_uniforme
from algoritmos.avara import avara
from algoritmos.a_star import a_star
from helpers import SearchType
import time

def busqueda(search_type, matriz):
    initial_pos = (0,0)  # Posición inicial: valor 2 en la matriz
    goalsPos = []        # Posiciones de los valores 4 en la matriz

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == 2:
                initial_pos = (i, j)
            elif matriz[i][j] == 4:
                goalsPos.append((i, j))

    print(f"Posición inicial Dron: ({initial_pos[0]}, {initial_pos[1]})")
    print(f"Número de paquetes por recoger: {len(goalsPos)}")

    nodo_final = None
    nodos_expandidos = 0
    inicio = time.time() * 1000  # Tiempo inicial

    if SearchType(search_type) == SearchType.AMPLITUD:
        nodo_final, nodos_expandidos = amplitud(matriz, initial_pos, goalsPos)
    elif SearchType(search_type) == SearchType.COSTO_UNIFORME:
        nodo_final, nodos_expandidos = costo_uniforme(matriz, initial_pos, goalsPos)
    elif SearchType(search_type) == SearchType.AVARA:
        nodo_final, nodos_expandidos = avara(matriz, initial_pos, goalsPos)
    elif SearchType(search_type) == SearchType.A_START:
        nodo_final, nodos_expandidos = a_star(matriz, initial_pos, goalsPos)

    fin = time.time() * 1000  # Tiempo final
    tiempo_ejecucion = fin - inicio

    if nodo_final is None:
        print("❌ No se encontró ninguna ruta al objetivo.")
    else:
        print("✅ ¡Ruta encontrada!")

    return [nodo_final, nodos_expandidos, tiempo_ejecucion]

# Ejemplo de ejecución
# exampleValue = [
#     [1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
#     [1, 1, 0, 1, 0, 1, 0, 1, 1, 1],
#     [0, 2, 0, 3, 4, 4, 0, 0, 0, 0],
#     [0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
#     [0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
#     [3, 3, 0, 1, 0, 1, 1, 1, 1, 1],
#     [1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
#     [1, 1, 0, 1, 1, 1, 1, 1, 1, 0],
#     [1, 1, 0, 0, 0, 0, 4, 0, 0, 0],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# ]

#busqueda(SearchType.A_START, exampleValue)
