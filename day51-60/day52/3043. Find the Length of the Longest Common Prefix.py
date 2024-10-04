class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        set1=set(map(str,arr1))
        set2=set(map(str,arr2))

        all_prefix_set1=set()
        for elem in set1:
            for i in range(1,len(elem)+1):
                all_prefix_set1.add(elem[:i])
        
        longest_common_prefix=0
        for elem in set2:
            for i in range(1,len(elem)+1):
                if elem[:i] in all_prefix_set1:
                    longest_common_prefix=max(longest_common_prefix,i)

        return longest_common_prefix
    
sol=Solution()
arr1 = [1,2,3]
arr2 = [4,4,4]        
print(sol.longestCommonPrefix(arr1,arr2))