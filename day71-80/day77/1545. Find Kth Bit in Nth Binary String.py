class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def findBit(n, k):
            if n == 1:
                return '0'      
            length = (1 << n) - 1          
            if k == (length // 2) + 1:
                return '1'
            if k < (length // 2) + 1:
                  return findBit(n - 1, k)
            return '1' if findBit(n - 1, length - k + 1) == '0' else '0'
        return findBit(n, k)
    
sol=Solution()
print(sol.findKthBit(4,11))