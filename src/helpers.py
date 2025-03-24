from enum import Enum

class SearchType(Enum):
    COSTO_UNIFORME = 'Costo uniforme'
    AMPLITUD = 'Amplitud'
    AVARA = 'Avara'
    A_START = 'A*'
    PROFUNDIDAD = 'Profundidad evitando ciclos'

MAP_SIZE = 10