class Solution(object):
    def xorQueries(self, arr, queries):
        """
        :type arr: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        prefix=[0]*(len(arr)+1)
        prefix[1]=arr[0]
        for i in range(1,len(arr)):
            prefix[i+1]=prefix[i]^arr[i]
        res=[]
        for query in queries:
            [i,j]=query
            res.append(prefix[i]^prefix[j+1])
        return res

sol=Solution()
arr=[4,8,2,10]
queries=[[2,3],[1,3],[0,0],[0,3]]
print(sol.xorQueries(arr,queries))