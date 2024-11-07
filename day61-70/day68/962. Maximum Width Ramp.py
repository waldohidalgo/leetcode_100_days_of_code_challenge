from typing import List
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        max_width = 0
        
        for i in range(len(nums)):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)
       
        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[j] >= nums[stack[-1]]:
                if nums[stack[0]]<=nums[j]:
                    return max(max_width, j - stack[0])
                max_width = max(max_width, j - stack.pop())

        return max_width
    

sol=Solution()
# nums = [9,8,1,0,1,9,4,0,4,1]
# nums=[10,10,10,7,1,6,2,1,7]
nums=[3,28,15,1,4,12,6,19,8,15,3,9,6,4,13,12,6,12,10,1,2,1,4,1,4,0,0,1,1,0]
# nums=[1,1,1,1]
print(sol.maxWidthRamp(nums))
# print(list(enumerate(nums)))
            