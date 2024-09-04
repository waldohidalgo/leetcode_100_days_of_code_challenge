class Solution(object):
    def rangeSum(self, nums, n, left, right):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        arr=[]
        i=0
        j=0
        suma=0
        while i<n:
            while j<n:
                suma+=nums[j]
                arr.append(suma)
                j+=1
            suma=0
            i+=1
            j=i
        arrSum=sorted(arr)[left-1:right]
        return sum(arrSum)%(10**9+7)
        
sol=Solution()
print(sol.rangeSum([1,2,3,4],4,1,10))
