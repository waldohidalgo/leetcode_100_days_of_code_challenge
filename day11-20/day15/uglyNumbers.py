class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        uglyNumbersSet=[1]
        i=1
        currentUgly=None
        while i<=n:
            uglyNumbersSet=list(dict.fromkeys(uglyNumbersSet))
            uglyNumbersSet.sort(reverse=True)
            currentUgly=uglyNumbersSet.pop()
            uglyNumbersSet.append(currentUgly*2)
            uglyNumbersSet.append(currentUgly*3)
            uglyNumbersSet.append(currentUgly*5)
            i+=1

        return currentUgly
    
sol=Solution()
print(sol.nthUglyNumber(10))

