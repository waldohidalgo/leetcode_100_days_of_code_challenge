from typing import List
import heapq
from math import ceil
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = []
        score=0
        for num in nums:
            heapq.heappush(heap, num*-1)
        while k>0:
            max_elem=-heapq.heappop(heap)
            score+=max_elem
            new_elem=ceil(max_elem/3)
            heapq.heappush(heap, new_elem*-1)
            k-=1
        return score

sol=Solution()
nums = [1,10,3,3,3]
k = 3

print(sol.maxKelements(nums,k))