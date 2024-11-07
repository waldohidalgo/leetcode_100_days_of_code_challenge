from typing import List

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo = [[-1] * n for _ in range(m)]
        
        def dfs(i, j):
            if memo[i][j] != -1:
                return memo[i][j]
            
            max_moves = 0
            
            for di, dj in [(-1, 1), (0, 1), (1, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] > grid[i][j]:
                    max_moves = max(max_moves, 1 + dfs(ni, nj))
            
            memo[i][j] = max_moves
            return max_moves
        
        
        return max(dfs(i, 0) for i in range(m))


    def maxMoves2(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp=[[0]*n for _ in range(m)]
        for j in range(n-2,-1,-1):
            for i in range(m):
                current_value=grid[i][j]
                neighbors=[]
                if i>0 and grid[i-1][j+1]>current_value:
                    neighbors.append(dp[i-1][j+1])
                if grid[i][j+1]>current_value:
                    neighbors.append(dp[i][j+1])
                if i+1<m and grid[i+1][j+1]>current_value:
                    neighbors.append(dp[i+1][j+1])
                dp[i][j]=max(neighbors,default=0)+(1 if neighbors else 0)
        
        return max([row[0] for row in dp ])
                    
sol=Solution()
#grid =[[3,2,4],[2,1,9],[1,1,7]]
#grid = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]
grid=[[65,200,263,220,91,183,2,187,175,61,225,120,39],
      [111,242,294,31,241,90,145,25,262,214,145,71,294],
      [152,25,240,69,279,238,222,9,137,277,8,143,143],
      [189,31,86,250,20,63,188,209,75,22,127,272,110],
      [122,94,298,25,90,169,68,3,208,274,202,135,275],
      [205,20,171,90,70,272,280,138,142,151,80,122,130],
      [284,272,271,269,265,134,185,243,247,50,283,20,232],
      [266,236,265,234,249,62,98,130,122,226,285,168,204],
      [231,24,256,101,142,28,268,82,111,63,115,13,144],
      [277,277,31,144,49,132,28,138,133,29,286,45,93],
      [163,96,25,9,3,159,148,59,25,81,233,127,12],
      [127,38,31,209,300,256,15,43,74,64,73,141,200]]
print(sol.maxMoves(grid))