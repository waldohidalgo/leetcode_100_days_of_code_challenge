from typing import List

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        hash_map = set(nums)
        init_checked=set()
        max_streak = -1
        for num in nums:
            if num in init_checked:
                continue
            if int(num**0.5) ** 2 == num and int(num**0.5) in hash_map:
                continue
            streak=1
            current=num
            while current**2 in hash_map:
                streak+=1
                current=current**2
            if streak>=2 and streak>max_streak:
                max_streak=streak
            if max_streak==5:
                return max_streak
            init_checked.add(num)
        return max_streak


sol=Solution()
nums=[4,3,6,16,8,2]
print(sol.longestSquareStreak(nums))