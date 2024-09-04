import copy

class Solution(object):
    def minDays(self, gridArgs):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        m=len(gridArgs)
        n=len(gridArgs[0])
        
        def countIslands(grid):
            def dfs(x,y):
                if x<0 or y<0 or x>=m or y>=n or grid[x][y]==0:
                    return
                grid[x][y]=0
                dfs(x+1,y)
                dfs(x,y+1)
                dfs(x-1,y)
                dfs(x,y-1)
            
            m=len(grid)
            n=len(grid[0])
            count=0
            for i in range(m):
                for j in range(n):
                    if grid[i][j]==1:
                        dfs(i,j)
                        count+=1

            return count
        
        count=countIslands(copy.deepcopy(gridArgs))
        
        if count==0 or count!=1:
            return 0
        else:
            for i in range(m):
                for j in range(n):
                    copyGrid=copy.deepcopy(gridArgs)
                    if copyGrid[i][j]==1:
                        copyGrid[i][j]=0
                        if countIslands(copyGrid) != 1:
                            return 1

            return 2   
    
    
sol=Solution()
grid = [[0,0,0],[0,0,0],[0,0,0]]
print(sol.minDays(grid))