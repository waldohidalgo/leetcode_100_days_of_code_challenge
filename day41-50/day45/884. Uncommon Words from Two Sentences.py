class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        dictCounter={}
        for word in s1.split():
            dictCounter[word]=dictCounter.get(word,[0,0])
            dictCounter[word][0]=dictCounter[word][0]+1
        for word in s2.split():
            dictCounter[word]=dictCounter.get(word,[0,0])
            dictCounter[word][1]=dictCounter[word][1]+1
        return [word for word,count in dictCounter.items() if count[0]==0 and count[1]==1 or count[0]==1 and count[1]==0]
    
sol=Solution()
s1="apple apple"
s2="banana"
print(sol.uncommonFromSentences(s1,s2))