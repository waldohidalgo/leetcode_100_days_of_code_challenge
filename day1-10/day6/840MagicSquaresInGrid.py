class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows=len(grid)
        cols=len(grid[0])

        def isMagicSquare(square):
            # square is 3x3 list            
            # check if square has distinct elements from 1 to 9
            setElements=set([x for row in square for x in row])
            if not setElements==set(range(1,10)):
                return False
            else:
                # check if square is magic
                arrSumHorizontal=[sum(row) for row in square]
                arrSumVertical=[sum(col) for col in zip(*square)]
                arrSumDiagonal=[sum([square[i][i] for i in range(3)]),sum([square[i][2-i] for i in range(3)])]
                setSum=set(arrSumHorizontal+arrSumVertical+arrSumDiagonal)
                if len(setSum)==1:
                    return True
                else:
                    return False
                
        if rows<3 or cols<3:
            return 0
        else: 
            count=0
            for i in range(0,rows-2):
                for j in range(0,cols-2):
                    square=[[grid[i][j],grid[i][j+1],grid[i][j+2]],[grid[i+1][j],grid[i+1][j+1],grid[i+1][j+2]],[grid[i+2][j],grid[i+2][j+1],grid[i+2][j+2]]]
                    if isMagicSquare(square):
                        count+=1
            return count
        
sol=Solution()
grid=[[8]]
print(sol.numMagicSquaresInside(grid))