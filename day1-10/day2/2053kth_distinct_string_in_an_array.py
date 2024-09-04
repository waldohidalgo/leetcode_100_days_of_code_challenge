class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        arrDistinct = []
        i=0
        while i<len(arr):
            if arr.count(arr[i])==1:
                arrDistinct.append(arr[i])
            i+=1
        
        if k > len(arrDistinct):
            return ''
        else:
            return arrDistinct[k-1]
       
sol=Solution()
print(sol.kthDistinct(["aaa","aa","a"], 3))