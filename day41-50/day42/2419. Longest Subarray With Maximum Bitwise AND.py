class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxElement = max(nums)
        maxCount=0
        count=0
        for num in nums:
            if num==maxElement:
                count+=1
                maxCount=max(maxCount,count)
            else:
                count=0
        return maxCount





sol=Solution()
nums=[3,3,3,3,3]

print(sol.longestSubarray(nums))