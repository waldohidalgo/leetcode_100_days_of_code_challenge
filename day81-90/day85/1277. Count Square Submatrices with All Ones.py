from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        total_squares = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    if i > 0 and j > 0:
                        matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
                    total_squares += matrix[i][j]
        
        return total_squares
    
sol=Solution()
matrix = [
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
print(sol.countSquares(matrix))