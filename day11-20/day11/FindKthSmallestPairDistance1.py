class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sizeList=len(nums)
        maxElem=max(nums)
        distanceList=[0]*(maxElem+1)
        for i in range(sizeList):
            for j in range(i+1,sizeList):
                distanceList[abs(nums[j]-nums[i])]+=1
        for dist in range(maxElem+1):
            k-=distanceList[dist]
            if k<=0:
                return dist
        return -1
    
sol=Solution()
nums=[1,6,1]
k=35
print(sol.smallestDistancePair(nums,k))