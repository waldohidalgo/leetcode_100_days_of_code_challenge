class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        acumulator={5:0,10:0,20:0}

        for bill in bills:
            if bill==5:
                acumulator[5]+=1
            elif bill==10:
                if acumulator[5]==0:
                    return False
                acumulator[5]-=1
                acumulator[10]+=1
            else:
                if acumulator[10]>0 and acumulator[5]>0:
                    acumulator[10]-=1
                    acumulator[5]-=1
                elif acumulator[5]>=3:
                    acumulator[5]-=3
                else:
                    return False
        return True
    
sol=Solution()
print(sol.lemonadeChange([5,5,10,10,20]))

        