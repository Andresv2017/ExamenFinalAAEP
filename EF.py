import heapq


class RedTransporte:
    """
    Representa la red de transporte como un grafo dirigido con pesos en los arcos.
    """

    def __init__(self, nodos):
        self.nodos = nodos
        self.grafo = {nodo: [] for nodo in range(nodos)}

    def agregar_arco(self, origen, destino, peso):
        """
        Agrega un arco dirigido con un peso al grafo.
        """
        self.grafo[origen].append((destino, peso))

    def ruta_mas_rapida_dijkstra(self, inicio, fin):
        """
        Encuentra la ruta más rápida utilizando el algoritmo de Dijkstra.
        """
        distancias = [float('inf')] * self.nodos
        distancias[inicio] = 0
        prioridad = [(0, inicio)]  # (distancia, nodo)
        padre = [-1] * self.nodos

        while prioridad:
            distancia_actual, nodo_actual = heapq.heappop(prioridad)

            if distancia_actual > distancias[nodo_actual]:
                continue

            for vecino, peso in self.grafo[nodo_actual]:
                nueva_distancia = distancia_actual + peso

                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    padre[vecino] = nodo_actual
                    heapq.heappush(prioridad, (nueva_distancia, vecino))

        # Reconstruir la ruta
        ruta = []
        actual = fin
        while actual != -1:
            ruta.append(actual)
            actual = padre[actual]

        return ruta[::-1], distancias[fin]


def main():
    print("Configuración de la red de transporte")

    # Entrada: número de nodos
    nodos = int(input("Ingrese el número de nodos en la red: "))
    red = RedTransporte(nodos)

    # Entrada: definir arcos
    print("Ingrese los arcos de la red (formato: origen destino peso). Escriba 'fin' para terminar:")
    while True:
        entrada = input("Arco: ")
        if entrada.lower() == "fin":
            break
        try:
            origen, destino, peso = map(int, entrada.split())
            if origen < 0 or origen >= nodos or destino < 0 or destino >= nodos or peso < 0:
                print("Entrada inválida. Asegúrese de que los nodos estén dentro del rango y el peso sea positivo.")
                continue
            red.agregar_arco(origen, destino, peso)
        except ValueError:
            print("Entrada inválida. Use el formato: origen destino peso")

    # Entrada: nodo inicial y final
    inicio = int(input("Ingrese el nodo inicial: "))
    fin = int(input("Ingrese el nodo final: "))

    if inicio < 0 or inicio >= nodos or fin < 0 or fin >= nodos:
        print("Nodos fuera de rango. Ejecución terminada.")
        return

    # Calcular la ruta más rápida
    ruta, distancia = red.ruta_mas_rapida_dijkstra(inicio, fin)
    print(f"Ruta más rápida: {ruta} con distancia {distancia}")


if __name__ == "__main__":
    main()

