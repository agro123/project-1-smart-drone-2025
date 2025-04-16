from algoritmos.amplitud import amplitud
from algoritmos.costo_uniforme import costo_uniforme
from algoritmos.avara import avara
from algoritmos.a_star import a_star
from helpers import SearchType

#tipo_busqueda, matriz => resultados (por definir su estructura)
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
    if SearchType(search_type) == SearchType.AMPLITUD:
        return amplitud(matriz, initial_pos, goalsPos)
    if SearchType(search_type) == SearchType.COSTO_UNIFORME:
        return costo_uniforme(matriz, initial_pos, goalsPos)
    if SearchType(search_type) == SearchType.AVARA:
        return avara(matriz, initial_pos, goalsPos)
    if SearchType(search_type) == SearchType.A_START:
        return a_star(matriz, initial_pos, goalsPos)
    else:
        print('to do')
        return None


exampleValue = [[1, 1, 0, 0, 0, 0, 0, 1, 1, 1], [1, 1, 0, 1, 0, 1, 0, 1, 1, 1], [0, 2, 0, 3, 4, 4, 0, 0, 0, 0], [0, 1, 1, 1, 0, 1, 1, 1, 1, 0], [0, 1, 1, 1, 0, 0, 0, 0, 0, 0], [3, 3, 0, 1, 0, 1, 1, 1, 1, 1], [1, 1, 0, 1, 0, 0, 0, 0, 0, 0], [1, 1, 0, 1, 1, 1, 1, 1, 1, 0], [1, 1, 0, 0, 0, 0, 4, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
busqueda(SearchType.A_START, exampleValue)