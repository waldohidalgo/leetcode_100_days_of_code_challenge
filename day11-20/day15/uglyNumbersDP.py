class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        uglyNumbers=[1]+[None]*(n-1)
        indexMultipleOf2=0
        indexMultipleOf3=0
        indexMultipleOf5=0
        nextMultipleOf2=2
        nextMultipleOf3=3
        nextMultipleOf5=5
        for i in range(1,n):
            uglyNumbers[i]=min(nextMultipleOf2,nextMultipleOf3,nextMultipleOf5)
            if uglyNumbers[i]==nextMultipleOf2:
                indexMultipleOf2+=1
                nextMultipleOf2=uglyNumbers[indexMultipleOf2]*2
            if uglyNumbers[i]==nextMultipleOf3:
                indexMultipleOf3+=1
                nextMultipleOf3=uglyNumbers[indexMultipleOf3]*3
            if uglyNumbers[i]==nextMultipleOf5:
                indexMultipleOf5+=1
                nextMultipleOf5=uglyNumbers[indexMultipleOf5]*5

        return uglyNumbers[-1]
    

sol=Solution()
print(sol.nthUglyNumber(8))