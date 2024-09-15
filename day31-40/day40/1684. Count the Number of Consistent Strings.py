class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        count=0
        for word in words:
            i=0
            while i<len(word):
                if word[i] not in allowed:
                    break
                i+=1
                if i==len(word):
                    count+=1            
        return count
        


sol=Solution()
allowed="abc"
words=["a","b","c","ab","ac","bc","abc"]
print(sol.countConsistentStrings(allowed,words))