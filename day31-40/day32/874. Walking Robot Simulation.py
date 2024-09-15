class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        obstacle_set = set(map(tuple, obstacles))
        directions=[(0, 1), (1, 0), (0, -1), (-1, 0)]
        current_direction = 0
        i,j=0,0
        max_distance=0
        for command in commands:
            if command>0:
                for _ in range(command):
                    new_i = i + directions[current_direction][0]
                    new_j = j + directions[current_direction][1]
                    if (new_i, new_j) not in obstacle_set:
                        i, j = new_i, new_j
                        max_distance = max(max_distance, i**2 + j**2)
                    else:
                        break
            if command==-1:
                current_direction = (current_direction + 1) % 4
            if command==-2:
                current_direction = (current_direction - 1) % 4
            max_distance = max(max_distance, i**2 + j**2)
        return max_distance




sol=Solution()
commands=[6,-1,-1,6]
obstacles=[]
print(sol.robotSim(commands, obstacles))
