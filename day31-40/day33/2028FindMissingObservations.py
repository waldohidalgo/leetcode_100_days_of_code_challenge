class Solution(object):
    def missingRolls(self, rolls, mean, n):
        """
        :type rolls: List[int]
        :type mean: int
        :type n: int
        :rtype: List[int]
        """
        m=len(rolls)
        sumRest=mean*(m+n)-sum(rolls)
        minLimit=n
        maxLimit=6*n

        if sumRest<minLimit or sumRest>maxLimit:
            return []
        else:
            residuo=sumRest%n
            if residuo==0:
                return [sumRest//n]*n
            else:
                return [sumRest//n+1]*residuo+[sumRest//n]*(n-residuo)
        
sol=Solution()
print(sol.missingRolls([3,2,4,3],4,2))