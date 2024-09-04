class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        min_value = float('inf')
        max_value = -float('inf')
        max_distance = 0

        for array in arrays:
            if max_value != -float('inf'):
                max_distance = max(max_distance, abs(array[-1] - min_value), abs(max_value - array[0]))
            
            min_value = min(min_value, array[0])
            max_value = max(max_value, array[-1])
        
        return max_distance 
    
sol=Solution() 

#arrays=[[-8,-7,-7,-5,1,1,3,4],[-2],[-10,-10,-7,0,1,3],[2]]
arrays=[[1,5],[3,4]]
print(sol.maxDistance(arrays))
            
        
        