class Solution:
    def makeFancyString(self, s: str) -> str:
        stack=[]
        for char in s:
            if (len(stack)>=2 
                and stack[-1]==stack[-2] 
                and stack[-1]==char):
                continue
            stack.append(char)
        return "".join(stack)
    

sol=Solution()
print(sol.makeFancyString("aaabaaaa"))