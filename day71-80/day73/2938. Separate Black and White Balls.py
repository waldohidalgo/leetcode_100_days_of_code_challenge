class Solution:
    def minimumSteps(self, s: str) -> int:
        counter=0
        inner_counter=0
        j=len(s)-1
        i=s.index('1') if '1' in s else 0
        while j>=i:
            if s[j]=='0':
                inner_counter+=1
            else:
                counter+=inner_counter
            j-=1
        return counter
    def minimumSteps2(self, s: str) -> int:
        i=0
        i_put=0
        counter=0
        for i in range(len(s)):
            if s[i]=='0':
                counter+=i-i_put
                i_put=i_put+1
        return counter  


sol=Solution()
print(sol.minimumSteps2("0101000001"))
            
