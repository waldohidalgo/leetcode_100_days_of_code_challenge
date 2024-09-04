import re
class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        def findGCD(a, b):
            a=abs(a)
            b=abs(b)
            if a==0:
                return b
            if b==0:
                return a
            if a>b:
                return findGCD(a%b, b)
            return findGCD(a, b%a) 
        def notEmpty(char):
            return char!=''

        nums=list(filter(notEmpty,re.split(r'(?=[-+])|\/',expression)))
        
        num=0
        den=1
        i=0
        while i<len(nums):
            currNum=int(nums[i])
            print(nums[i+1])
            currDen=int(nums[i+1])
            num=num*currDen+currNum*den
            den=den*currDen
            i+=2
        print(num,den)
        gcd=abs(findGCD(num,den))
        
        return str(num//gcd)+'/'+str(den//gcd)


sol=Solution()
print(sol.fractionAddition("-4/7-3/4+2/3"))