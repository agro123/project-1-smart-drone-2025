from nodo import Nodo, Movement
from collections import deque

def profundidad(matriz, pos=(0, 0), goals_positions=[]):
    stack = deque()
    nodo_inicial = Nodo(pos=pos, posicion_objetivos=goals_positions)
    stack.append(nodo_inicial)

    index = 0
    nodos_expandidos = 1

    while stack:
        index += 1
        print('Iteración', index)

        node = stack.popleft() # DFS usa .pop(), no .popleft()
        print("Posición", node.pos)

        # Verificar si se completaron los paquetes
        cajas_restantes = node.verificar_caja()
        print("Cajas restantes", cajas_restantes)
        if cajas_restantes == 0:
            node.mostrar_costo()
            node.mostrar_profundidad()
            print('Solución encontrada')
            return [node, nodos_expandidos]

        # Expandir
        movimientos = [
            Movement.LEFT,
            Movement.TOP,
            Movement.RIGHT,
            Movement.DOWN
        ]
        indexNode = 0
        for movimiento in movimientos:
            nueva_pos = node.ir(matriz, movimiento)
            if nueva_pos["valor"] != 1:  # No es un obstáculo
                nuevo_nodo = Nodo(
                    pos=nueva_pos["n_pos"],
                    padre=node,
                    profundidad=node.profundidad + 1,
                    costo=node.costo + nueva_pos["costo"],
                    operador=nueva_pos["operador"],
                    posicion_objetivos=node.posicion_objetivos
                )
                
                if not nuevo_nodo.evitar_ciclos():
                    nodos_expandidos += 1
                    stack.insert(indexNode, nuevo_nodo)
                    indexNode += 1

    print('Sin solución')
    return None