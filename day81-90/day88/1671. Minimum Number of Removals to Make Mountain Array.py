from typing import List
class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n=len(nums)
        lis=[1]*n
        lds=[1]*n

        for i in range(1,n):
            for j in range(i):
                if nums[j]<nums[i]:
                    lis[i]=max(lis[i],lis[j]+1)

        for i in range(n-2,-1,-1):
            for j in range(n-1,i,-1):
                if nums[j]<nums[i]:
                    lds[i]=max(lds[i],lds[j]+1)

        # solo considera las mountains de largo mayor o igual a 3
        return n-max([lis[i]+lds[i]-1 if lis[i]>1 and lds[i]>1 else 0 for i in range(n) ])
    
    def minimumMountainRemovals2(self, nums: List[int]) -> int:
        n=len(nums)
        lis=[0]*n
        lds=[0]*n
        aux=[]
        for i in range(n):
            index=bisect_left(aux,nums[i])
            if index<len(aux):
                lis[i]=index
            else:
                aux.append(nums[i])
            lis[i]=index+1
        aux=[]
        for i in range(n-1,-1,-1):
            index=bisect_left(aux,nums[i])
            if index<len(aux):
                lds[i]=index
            else:
                aux.append(nums[i])
            lds[i]=index+1
        return n-max([lis[i]+lds[i]-1 if lis[i]>1 and lds[i]>1 else 0 for i in range(n) ])

                 

sol=Solution()
#nums=[100,92,89,77,74,66,64,66,64]
nums = [2,1,1,5,6,2,3,1]
#nums=[1,3,1]
print(sol.minimumMountainRemovals(nums))