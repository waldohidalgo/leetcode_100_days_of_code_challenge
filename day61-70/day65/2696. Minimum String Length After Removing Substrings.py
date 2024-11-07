import re

class Solution:
    def minLength(self, s: str) -> int:
       # tiempo de complejidad: O(n**2)
       while re.search(r"AB|CD",s):
           s=re.sub(r"(AB|CD)",'',s)
       return len(s)
    
    def minLength2(self, s: str) -> int:
        letras=[]
        for char in s:
            if char=='A' or char =='C':
                letras.append(char)
            elif char=='B' and letras and letras[-1]=='A':
                letras.pop()
            elif char=='D' and letras and letras[-1]=='C':
                letras.pop()
            else:
                letras.append(char)
        return len(letras)


s = "D"
print(Solution().minLength2(s))