class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        suffixSum=piles[:]
        for i in range(len(piles)-2,-1,-1):
            suffixSum[i]+=suffixSum[i+1]
        def maxStones(suffixSum,maxTillNow,currIndex,memo):
            if currIndex+2*maxTillNow>=len(suffixSum):
                return suffixSum[currIndex]
            else:
                if memo[currIndex][maxTillNow]>0:
                    return memo[currIndex][maxTillNow]
                else:
                    res=float('inf')
                    for i in range(1,2*maxTillNow+1):
                        res=min(res,maxStones(suffixSum,max(maxTillNow,i),currIndex+i,memo))
                    memo[currIndex][maxTillNow]=suffixSum[currIndex]-res
                    return suffixSum[currIndex]-res

        return maxStones(suffixSum,1,0,[[0 for _ in range(len(piles))] for _ in range(len(piles))])
    

sol=Solution()
print(sol.stoneGameII([1,2,100]))

    

