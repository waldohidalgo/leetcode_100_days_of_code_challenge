import heapq
from collections import defaultdict

class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start_node: int
        :type end_node: int
        :rtype: float
        """
        graph = defaultdict(list)
        for (u, v), prob in zip(edges, succProb):
            graph[u].append((v, prob))
            graph[v].append((u, prob))
    

        max_heap = [(-1.0, start_node)]  
        heapq.heapify(max_heap)
        probabilities = {i: 0 for i in range(n)}
        probabilities[start_node] = 1.0
    
        while max_heap:
            curr_prob, node = heapq.heappop(max_heap)
            curr_prob = -curr_prob
            if node == end_node:
                return curr_prob
            for neighbor, edge_prob in graph[node]:
                new_prob = curr_prob * edge_prob
                if new_prob > probabilities[neighbor]:
                    probabilities[neighbor] = new_prob
                    heapq.heappush(max_heap, (-new_prob, neighbor))
    
        return 0.0
    
sol=Solution()
print(sol.maxProbability(3,[[0,1]],[0.5],0,2))