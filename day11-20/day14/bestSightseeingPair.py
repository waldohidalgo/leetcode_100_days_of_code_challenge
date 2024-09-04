class Solution(object):
    def maxScoreSightseeingPair(self, values):
        """
        :type values: List[int]
        :rtype: int
        """
        maxScore = 0
        acc=values[0]+0
        for i in range(1,len(values)):
            if acc+values[i]-i>maxScore:
                maxScore=acc+values[i]-i
            if values[i]+i>acc:
                acc=values[i]+i
        return maxScore
    
sol=Solution()
print(sol.maxScoreSightseeingPair([1,2]))