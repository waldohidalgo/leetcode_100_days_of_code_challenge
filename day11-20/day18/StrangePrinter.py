
class Solution:
    def strangePrinter(self, s):
        
        def removeDuplicates(s):
            uniqueChars=s[0]
            for i in range(1,len(s)):
                if s[i]!=s[i-1]:
                    uniqueChars+=s[i]
                
            return uniqueChars
        
        s=removeDuplicates(s)
        n=len(s)
        memo=[[-1]*n for _ in range(n)]
        def minimumTurns(start,end,s,memo):
            if start>end:
                return 0
            if memo[start][end]!=-1:
                return memo[start][end]
            minTurns=1+minimumTurns(start+1,end,s,memo) # peor caso ejemplo: ab => a,b
            for i in range(start+1,end+1):
                if s[start]==s[i]:
                    minTurns=min(minTurns,minimumTurns(start,i-1,s,memo)+minimumTurns(i+1,end,s,memo))
            memo[start][end]=minTurns
            return minTurns
        return minimumTurns(0,n-1,s,memo)


sol=Solution()

print(sol.strangePrinter("aba"))

        
