class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        if m*n != len(original):
            return []
        return [original[i*n:(i+1)*n] for i in range(m)]
    
sol=Solution()
print(sol.construct2DArray([1,2],1,1))