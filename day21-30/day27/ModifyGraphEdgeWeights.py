from typing import List

class Solution:
    INF=1e9+1
    def djkta(
        self, edges: List[List[int]], n: int, source: int, destination: int
    ) -> int:
        adj_matrix = [[self.INF] * n for _ in range(n)]
        min_distance = [self.INF] * n
        visited = [False] * n
        min_distance[source] = 0
        for nodeA, nodeB, weight in edges:
            if weight != -1:
                adj_matrix[nodeA][nodeB] = weight
                adj_matrix[nodeB][nodeA] = weight
      
        for _ in range(n):
            nearest_unvisited_node = -1
            for i in range(n):
                if not visited[i] and (
                    nearest_unvisited_node == -1
                    or min_distance[i] < min_distance[nearest_unvisited_node]
                ):
                    nearest_unvisited_node = i
            visited[nearest_unvisited_node] = True
            for v in range(n):
                min_distance[v] = min(
                    min_distance[v],
                    min_distance[nearest_unvisited_node]
                    + adj_matrix[nearest_unvisited_node][v],
                )
        
        return min_distance[destination]
    def modifiedGraphEdges(
        self,
        n: int,
        edges: List[List[int]],
        source: int,
        destination: int,
        target: int,
    ) -> List[List[int]]:

        current_shortest_distance = self.djkta(
            edges, n, source, destination
        )

        if current_shortest_distance < target:
            return []
        matches_target = current_shortest_distance == target

        for edge in edges:
            if edge[2] > 0:
                continue
            edge[2] = self.INF if matches_target else 1
            if not matches_target:
                new_distance = self.djkta(edges, n, source, destination)
                if new_distance <= target:
                    matches_target = True
                    edge[2] += target - new_distance

        return edges if matches_target else []


    


sol=Solution()
n = 5
edges = [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]]
source = 0
destination = 1
target = 216

print(sol.modifiedGraphEdges(n, edges, source, destination, target))