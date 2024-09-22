class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        
        memo={}
        def divideAndConquer(expression):
            if expression in memo:
                return memo[expression]
            if expression.isdigit():
                return [int(expression)]
            res=[]
            for i in range(len(expression)):
                if expression[i] in "+-*":
                    left=divideAndConquer(expression[:i])
                    right=divideAndConquer(expression[i+1:])
                    for l in left:
                        for r in right:
                            if expression[i]=='*':
                                res.append(l*r)
                            elif expression[i]=='-':
                                res.append(l-r)
                            else:
                                res.append(l+r)
            memo[expression]=res
            return res
    
        return divideAndConquer(expression)
    
sol=Solution()
print(sol.diffWaysToCompute("2*3-4*5"))