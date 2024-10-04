class Solution(object):
    def minExtraChar(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: int
        """
        words=set(dictionary)
        # el array dp almacena la cantidad de caracteres que faltan 
        # para completar la palabra hasta el indice i considerando las palabras de dictionary
        dp=[0]*(len(s)+1)
        for i in range(1,len(s)+1):
            dp[i]=dp[i-1]+1
            for word in words:
                if s[i-len(word):i]==word:
                    dp[i]=min(dp[i],dp[i-len(word)])
        print(dp)
        return dp[-1]
    
s = "leetcode"
dictionary = ["leetcode"]

sol=Solution()
print(sol.minExtraChar(s,dictionary))