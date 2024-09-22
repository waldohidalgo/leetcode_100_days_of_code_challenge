class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def count_steps(prefix, n):
            """Cuenta cuántos números hay en el subárbol con el prefijo dado"""
            steps = 0
            first = prefix
            last = prefix
            while first <= n:
                steps += 1+min(n, last) - first
                first *= 10
                last = last * 10 + 9
            return steps
        
        current = 1
        k -= 1  
        while k > 0:
            steps = count_steps(current, n)
            if steps <= k:
                k -= steps
                current += 1
            else:
                current *= 10
                k -= 1                
        return current
    
sol=Solution()
n=2     
k=2
print(sol.findKthNumber(n,k))