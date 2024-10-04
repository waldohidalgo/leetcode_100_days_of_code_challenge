from typing import List

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        frequencies=[0]*k
        for num in arr:
            frequencies[(num%k+k)%k]+=1
        if frequencies[0]%2!=0:
            return False
        if k%2==0 and frequencies[k//2]%2!=0:
            return False
        for i in range(1,k//2+1):
            if k%2==0 and i==k//2:
                continue
            if frequencies[i]!=frequencies[k-i]:
                return False        
        return True
                
sol=Solution()

arr =[-1,-1,-1,-1,2,2,-2,-2]
k = 3

print(sol.canArrange(arr,k))