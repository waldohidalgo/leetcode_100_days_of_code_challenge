from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        suma_total = sum(nums)
        residuo_total = suma_total % p

        if residuo_total == 0:
            return 0

        suma = 0
        prefix_sum = {0: 0}
        min_length=float('inf')
        for i,num in enumerate(nums,1):
            suma += num
            target_residuo=(suma-suma_total)%p
            residuo=suma%p
            if target_residuo in prefix_sum: 
                min_length=min(min_length,i-prefix_sum[target_residuo])

            prefix_sum[residuo]=i

        print(prefix_sum)
        if min_length==len(nums):
            return -1
        return min_length
            

sol=Solution()
nums = [3,1,4,2]
p = 7
print(sol.minSubarray(nums,p))