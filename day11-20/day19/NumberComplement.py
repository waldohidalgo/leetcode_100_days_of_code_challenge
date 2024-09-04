class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        binario = bin(num)[2:]
        res=2**len(binario)-1-num
        return res
    
sol=Solution()
print(sol.findComplement(1))