from collections import deque
class Solution(object):
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """
        directions=[(1,0),(0,1),(-1,0),(0,-1)]

        def isCellLand(x, y, grid):
            if x<0 or y<0 or x>=len(grid) or y>=len(grid[0]):
                return False
            return grid[x][y]==1
        
        def bfs(x, y, grid1, grid2, visited):
            isSubIsland=True
            queue=deque([(x,y)])
            visited[x][y]=1
            while queue:
                x,y=queue.popleft()
                if grid1[x][y]==0:
                    isSubIsland=False
                
                for dx, dy in directions:
                    nx, ny=x+dx, y+dy
                    if isCellLand(nx, ny, grid2) and not visited[nx][ny]:
                        queue.append((nx,ny))
                        visited[nx][ny]=1
            return isSubIsland
        
        visited=[[0]*len(grid2[0]) for _ in range(len(grid2))]
        subIslandsCount=0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if isCellLand(i, j, grid2) and not visited[i][j]:
                    if bfs(i, j, grid1, grid2, visited):
                        subIslandsCount+=1
        return subIslandsCount
    
grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
sol=Solution()

print(sol.countSubIslands(grid1, grid2))