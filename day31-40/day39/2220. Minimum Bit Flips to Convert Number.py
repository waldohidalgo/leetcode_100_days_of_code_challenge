class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        result=start^goal
        return bin(result).count('1')
    
sol=Solution()
print(sol.minBitFlips(3,4))