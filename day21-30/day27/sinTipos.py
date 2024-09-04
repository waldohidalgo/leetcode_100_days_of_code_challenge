import heapq

class Solution:
    INF = int(2e9)

    def modifiedGraphEdges(self, n, edges, source, destination, target):
        """
        - n: Número de nodos en el grafo.
        - edges: Lista de aristas, cada una representada como [u, v, w], donde u y v son nodos,
                 y w es el peso de la arista. Si w es -1, el peso es desconocido y debe ser modificado.
        - source: Nodo de origen para el cálculo de la distancia.
        - destination: Nodo de destino para el cálculo de la distancia.
        - target: Distancia objetivo que se desea lograr.

        Retorna:
        - Una lista de aristas modificadas que hace que la distancia más corta entre source
          y destination sea igual a target, o una lista vacía si no es posible.
        """
        graph = [[] for _ in range(n)]

        # Se construye grafico con pesos conocidos
        for u, v, w in edges:
            if w != -1:
                graph[u].append((v, w))
                graph[v].append((u, w))

        # Se calcula la distancia más corta inicial
        current_shortest_distance = self.dijkstra(graph, source, destination)

        # Si la distancia más corta es menor a target, no se puede alcanzar la distancia objetivo ya que ya existen pesos
        if current_shortest_distance < target:
            return []

        # Si la distancia más corta es igual a target, se puede alcanzar la distancia objetivo y el resto de pesos de nodos se actualizan a un valor infinito de modo que no interfieran en la solución
        if current_shortest_distance == target:
            for edge in edges:
                if edge[2] == -1:
                    edge[2] = self.INF
            return edges

        # Si la distancia más corta es mayor a target, entonces se intenta reducirla ajustando el peso de las aristas desconocidas inicialmente a 1, y se verifica si es posible ajustar el peso de esa arista para que la nueva distancia sea igual a target
        for i, (u, v, w) in enumerate(edges):
            if w != -1:
                continue

            # Establecer el peso de la arista a 1 inicialmente
            edges[i][2] = 1
            graph[u].append((v, 1))
            graph[v].append((u, 1))

            # Recalcular la distancia más corta con el peso de arista actualizado
            new_distance = self.dijkstra(graph, source, destination)

            if new_distance <= target:
                edges[i][2] += target - new_distance

                # Actualizar aristas restantes con peso -1 a un valor imposible
                for j in range(i + 1, len(edges)):
                    if edges[j][2] == -1:
                        edges[j][2] = self.INF
                return edges
        return []

    def dijkstra(self, graph, src, destination):
        """
        Calcula la distancia más corta desde el nodo src hasta el nodo destination
        utilizando el algoritmo de Dijkstra.

        Parámetros:
        - graph: Grafo representado como una lista de listas de tuplas (nodo, peso).
        - src: Nodo de origen.
        - destination: Nodo de destino.

        Retorna:
        - La distancia más corta entre src y destination.
        """
        min_distance = [self.INF] * len(graph)
        min_distance[src] = 0
        min_heap = [(0, src)]  # (distancia, nodo)

        while min_heap:
            d, u = heapq.heappop(min_heap)
            if d > min_distance[u]:
                continue
            for v, w in graph[u]:
                if d + w < min_distance[v]:
                    min_distance[v] = d + w
                    heapq.heappush(min_heap, (min_distance[v], v))
        return min_distance[destination]

# Ejemplo de uso
sol = Solution()
n = 5
edges = [[4, 1, -1], [2, 0, -1], [0, 3, -1], [4, 3, -1]]
source = 0
destination = 1
target = 216

print(sol.modifiedGraphEdges(n, edges, source, destination, target))
