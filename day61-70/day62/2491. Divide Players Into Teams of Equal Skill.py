from typing import List
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        largo_total=len(skill)
        largo_medio=largo_total//2
        skill.sort()
        target_sum=sum(skill)//largo_medio
        chemistry=0
        
        for i in range(largo_medio):
            a,b=skill[i],skill[largo_total-i-1]
            if a+b==target_sum:
                chemistry+=a*b
            else:
                return -1

        return chemistry
    

sol=Solution()
skill = [1,1,2,3]
print(sol.dividePlayers(skill))