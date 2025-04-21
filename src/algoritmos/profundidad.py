from nodo import Nodo, Movement
from collections import deque

def profundidad(matriz, pos=(0, 0), goals_positions=[]):
    stack = deque()
    nodo_inicial = Nodo(pos=pos, posicion_objetivos=goals_positions)
    stack.append(nodo_inicial)

    index = 0
    nodos_expandidos = 1
    profundida_arbol = 0

    while stack:
        index += 1
        print('Iteración', index)

        node: Nodo = stack.pop()
        print("Posición", node.pos)

        cajas_restantes = node.verificar_caja()
        print("Cajas restantes", cajas_restantes)
        if len(cajas_restantes) == 0:
            node.mostrar_costo()
            node.mostrar_profundidad()
            print('Solución encontrada')
            return [node, nodos_expandidos, profundida_arbol]

        # Orden de prioridad:
        movimientos = [
            Movement.LEFT,
            Movement.TOP,
            Movement.RIGHT,
            Movement.DOWN,
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
                    posicion_objetivos=cajas_restantes
                )
                
                if not nuevo_nodo.evitar_ciclos():
                    nodos_expandidos += 1
                    stack.append(nuevo_nodo)  # Se respeta el orden por el reversed
                    if nuevo_nodo.profundidad > profundida_arbol:
                        profundida_arbol = nuevo_nodo.profundidad

    print('Sin solución')
    return None, nodos_expandidos, profundida_arbol
