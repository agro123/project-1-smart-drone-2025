from nodo import Nodo
from collections import deque

def insertar_ordenado(lista: deque[Nodo], nodo: Nodo) -> deque[Nodo]:
    for i, n in enumerate(lista):
        if nodo.costo < n.costo:
            lista.insert(i, nodo)
            return lista
    lista.append(nodo)
    return lista


def costo_uniforme(matriz, pos = [0,0], goals_number=1):
    queue = deque()
    nodo_inicial = Nodo(pos=pos)
    queue.append(nodo_inicial)

    index = 1

    while queue:
        print('Iteracion ', index)
        index = index + 1

        node = queue.popleft()

        #Verificar si se completaron los paquetes
        cajas = node.verificar_caja(matriz)
        print("Cajas ", node.cajas_obtenidas)
        print("Posición ", node.pos)
        if  cajas == goals_number:
            node.mostrar_costo()
            node.mostrar_profundidad()
            node.trayectoria()
            return node

        #Expandir
        movimientos = [
            node.ir_izquierda(matriz),
            node.ir_arriba(matriz),
            node.ir_derecha(matriz),
            node.ir_abajo(matriz)
        ]

        for movimiento in movimientos:
            if movimiento["valor"] != 1:  # No es un obstáculo
                nuevo_nodo = Nodo(
                    pos=movimiento["n_pos"],
                    padre=node,
                    profundidad=node.profundidad + 1,
                    costo=node.costo + movimiento["costo"],
                    cajas_obtenidas=node.cajas_obtenidas,
                    operador=movimiento["operador"]
                )
                if not nuevo_nodo.es_estado_repetido():
                    queue = insertar_ordenado(queue, nuevo_nodo)

    print('Sin solucion')
    return None
