class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        abc="abcdefghijklmnopqrstuvwxyz"
        s="".join([str(abc.index(x)+1) for x in s])
        i=0
        while i<k:
            val=0
            for x in s:
                val+=int(x)
            s=str(val)
            i+=1
        return int(s)


sol=Solution()
print(sol.getLucky("zbax",2))