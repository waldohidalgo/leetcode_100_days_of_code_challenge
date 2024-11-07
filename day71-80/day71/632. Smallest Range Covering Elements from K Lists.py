from typing import List
import heapq
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap=[]
        max_value=float('-inf')
        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i][0], i, 0))
            max_value=max(max_value, nums[i][0])

        res = [float('-inf'), float('inf')]

        while heap:
            min_value, i_list, index = heapq.heappop(heap)

            if res[1] - res[0] > max_value - min_value:
                res = [min_value, max_value]
        
            # si se acaban los elementos de la lista actual, salir del while
            if index + 1 == len(nums[i_list]):
                break
            else:
                next_val=nums[i_list][index+1]
                heapq.heappush(heap, (next_val, i_list, index + 1))
                max_value=max(max_value, next_val)

        return res
            
            
sol=Solution()

nums = [[1,2,3],[1,2,3],[1,2,3]]

print(sol.smallestRange(nums))