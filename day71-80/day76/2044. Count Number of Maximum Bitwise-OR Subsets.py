from typing import List
from itertools import combinations
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        count = 0
        for num in nums:
            max_or |= num
        
        for r in range(1, len(nums) + 1):
            for comb in combinations(nums, r):
                subset_or = 0
                for num in comb:
                    subset_or |= num
                if subset_or == max_or:
                    count += 1
        return count
    
sol=Solution()
nums=[2,2,2]

print(sol.countMaxOrSubsets(nums))