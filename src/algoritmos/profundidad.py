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

        node = stack.pop()
        print("Posición", node.pos)

        cajas_restantes = node.verificar_caja()
        print("Cajas restantes", cajas_restantes)
        if cajas_restantes == 0:
            node.mostrar_costo()
            node.mostrar_profundidad()
            print('Solución encontrada')
            return [node, nodos_expandidos]

        # Orden natural de prioridad: arriba → derecha → abajo → izquierda
        movimientos = [
            Movement.TOP,
            Movement.RIGHT,
            Movement.DOWN,
            Movement.LEFT
        ]
        # Para que se respete ese orden al usar pila (LIFO), insertamos al revés
        for movimiento in reversed(movimientos):
            nueva_pos = node.ir(matriz, movimiento)
            if nueva_pos["valor"] != 1:
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
                    stack.append(nuevo_nodo)  # Se respeta el orden por el reversed

    print('Sin solución')
    return None
