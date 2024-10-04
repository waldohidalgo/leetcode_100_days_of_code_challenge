from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        copy_arr=sorted(set(arr))
    
        dict_rank={elem:rank for rank,elem in enumerate(copy_arr,1)}

        return [dict_rank[elem] for elem in arr]
    
arr = [100,100,100]

print(Solution().arrayRankTransform(arr))	