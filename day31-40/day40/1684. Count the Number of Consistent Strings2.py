class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        isAllowed=[0]*26
        for c in allowed:
            isAllowed[ord(c)-97]=1
        count=0
        for word in words:
            for c in word:
                if not isAllowed[ord(c)-97]:
                    count+=1
                    break
            
        return len(words)-count
        


sol=Solution()
allowed="abc"
words=["a","b","c","ab","ac","bc","abc"]
print(sol.countConsistentStrings(allowed,words))