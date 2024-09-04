class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        col=len(points[0])
        rows=len(points)
        prev = points[0]
        for i in range(1, rows):
            leftMax=[0]*col
            rightMax=[0]*col
            leftMax[0]=prev[0]
            for j in range(1,col):
                leftMax[j]=max(prev[j],leftMax[j-1]-1)
            rightMax[col-1]=prev[col-1]
            for j in range(col-2,-1,-1):
                rightMax[j]=max(prev[j],rightMax[j+1]-1) 
            curr=[0]*col
            for j in range(col):
                curr[j]=max(leftMax[j],rightMax[j])+points[i][j]
            prev=curr
        return max(prev)

sol=Solution()
print(sol.maxPoints([[1,2,3],[1,5,1],[3,1,1]]))
            
