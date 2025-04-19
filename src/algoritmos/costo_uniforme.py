from nodo import Nodo, Movement
from collections import deque

def insertar_ordenado(lista: deque[Nodo], nodo: Nodo) -> deque[Nodo]:
    for i, n in enumerate(lista):
        if nodo.costo <= n.costo:
            lista.insert(i, nodo)
            return lista
    lista.append(nodo)
    return lista


def costo_uniforme(matriz, pos = (0,0), goals_positions = []):
    queue = deque()
    nodo_inicial = Nodo(pos=pos, posicion_objetivos=goals_positions)
    queue.append(nodo_inicial)

    index = 0
    nodos_expandidos = 1

    while queue:
        index = index + 1
        print('Iteracion ', index)

        node: Nodo = queue.popleft()
        print("Posición ", node.pos)

        #Verificar si se completaron los paquetes
        cajas_restantes = node.verificar_caja()
        print("Cajas restantes ", cajas_restantes)
        print("Posición ", node.pos)
        if  len(cajas_restantes) == 0:
            node.mostrar_costo()
            node.mostrar_profundidad()
            print('Solucion encontrada')
            return [node, nodos_expandidos]

        #Expandir
        movimientos = [
            Movement.LEFT,
            Movement.TOP,
            Movement.RIGHT,
            Movement.DOWN
        ]

        for movimiento in movimientos:
            nueva_pos = node.ir(matriz, movimiento)
            if nueva_pos["valor"] != 1:  # No es un obstáculo
                nuevo_nodo = Nodo(
                    pos=nueva_pos["n_pos"],
                    padre=node,
                    profundidad=node.profundidad + 1,
                    costo=node.costo + nueva_pos["costo"],
                    operador=movimiento,
                    posicion_objetivos=cajas_restantes
                )
                if not nuevo_nodo.evitar_ciclos():
                    nodos_expandidos = nodos_expandidos + 1
                    queue = insertar_ordenado(queue, nuevo_nodo)

    print('Sin solucion')
    return None, nodos_expandidos  # Cambiado: devuelve siempre una tupla
