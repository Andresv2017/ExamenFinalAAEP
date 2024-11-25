from itertools import permutations


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

    def calcular_peso_ruta(self, ruta):
        """
        Calcula el peso total de una ruta dada.
        """
        peso_total = 0
        for i in range(len(ruta) - 1):
            origen = ruta[i]
            destino = ruta[i + 1]
            # Buscar el peso del arco entre origen y destino
            for vecino, peso in self.grafo[origen]:
                if vecino == destino:
                    peso_total += peso
                    break
            else:
                # Si no existe un arco directo, la ruta no es válida
                return float('inf')
        return peso_total

    def ruta_mas_rapida_fuerza_bruta(self, inicio, fin):
        """
        Encuentra la ruta más rápida entre inicio y fin usando fuerza bruta.
        """
        # Generar todas las permutaciones posibles de los nodos
        nodos_intermedios = [nodo for nodo in range(self.nodos) if nodo != inicio and nodo != fin]
        rutas_posibles = permutations(nodos_intermedios)

        # Inicializar variables para la mejor ruta
        mejor_ruta = None
        menor_peso = float('inf')

        # Evaluar todas las rutas posibles
        for ruta_intermedia in rutas_posibles:
            ruta = [inicio] + list(ruta_intermedia) + [fin]
            peso = self.calcular_peso_ruta(ruta)
            if peso < menor_peso:
                menor_peso = peso
                mejor_ruta = ruta

        return mejor_ruta, menor_peso


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
    ruta, distancia = red.ruta_mas_rapida_fuerza_bruta(inicio, fin)
    if distancia == float('inf'):
        print("No hay ruta válida entre los nodos.")
    else:
        print(f"Ruta más rápida (Fuerza Bruta): {ruta} con distancia {distancia}")


if __name__ == "__main__":
    main()
