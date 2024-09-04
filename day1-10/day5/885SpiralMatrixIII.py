class Solution(object):
    # este algoritmo hace uso de la regularidad del recorrido en espiral
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        def isInBounds(r, c):
            return 0 <= r < rows and 0 <= c < cols
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  
        direction_index = 0
        current = (rStart, cStart)
        arrAllSteps = [current]

        total = 1  
        steps = 1  

        while total < rows * cols:
            for _ in range(2): 
                for _ in range(steps):
                    current = (current[0] + directions[direction_index][0],
                               current[1] + directions[direction_index][1])

                    if isInBounds(current[0], current[1]):
                        arrAllSteps.append(current)
                        total += 1
                        if total == rows * cols:
                            return arrAllSteps

                direction_index = (direction_index + 1) % 4  

            steps += 1 

        return arrAllSteps
    
sol=Solution()
print(sol.spiralMatrixIII(5,6,1,4))


            
