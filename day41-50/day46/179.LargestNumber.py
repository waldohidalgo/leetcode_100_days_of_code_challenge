from functools import cmp_to_key
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        numsToStr = [str(num) for num in nums]
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            else:
                return 0
        
        numsToStr = sorted(numsToStr, key=cmp_to_key(compare))
        
        greatestNum = "".join(numsToStr)
        return '0' if greatestNum[0] == '0' else greatestNum
    
sol=Solution()
nums=[0,0]
print(sol.largestNumber(nums))