from typing import List
from enum import Enum

def insertar_ordenado(lista: List[any], nodo: any) -> List[any]:
    for i, n in enumerate(lista):
        if nodo.costo < n.costo:
            lista.insert(i, nodo)
            return lista
    lista.append(nodo)
    return lista

class SearchType(Enum):
    COSTO_UNIFORME = 'Costo uniforme'
    AMPLITUD = 'Amplitud'
    AVARA = 'Avara'
    A_START = 'A*'
    PROFUNDIDAD = 'Profundidad evitando ciclos'

MAP_SIZE = 10