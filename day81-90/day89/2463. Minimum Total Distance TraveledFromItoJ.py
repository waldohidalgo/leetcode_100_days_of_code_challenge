from typing import List

class Solution:
    def minimumTotalDistance(self, robot, factory):
        factory = [f for f in factory if f[1] > 0]
        robot.sort()
        factory.sort(key=lambda x: x[0])

        m, n = len(robot), len(factory)
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        
        for j in range(n + 1):
            dp[0][j] = 0

        for i in range(1, m + 1):  
            for j in range(1, n + 1):
                dist_sum = 0
                
                for k in range(min(i, factory[j - 1][1])):  
                    dist_sum += abs(robot[i - k - 1] - factory[j - 1][0])
                    dp[i][j] = min(dp[i][j], dp[i - k - 1][j - 1] + dist_sum)
                
                dp[i][j] = min(dp[i][j], dp[i][j - 1])

        return dp[m][n]
    def minimumTotalDistanceRigth(self, robot: List[int], factory: List[List[int]]) -> int:
        factory = [f for f in factory if f[1] > 0]
        robot.sort()
        factory.sort()

        m, n = len(robot), len(factory)

        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
       
        for j in range(n + 1):
            dp[m][j] = 0

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dist_sum = 0
                
                for k in range(min(m - i, factory[j][1])):  
                    dist_sum += abs(robot[i + k] - factory[j][0])
                    dp[i][j] = min(dp[i][j], dp[i + k + 1][j + 1] + dist_sum)
                
                dp[i][j] = min(dp[i][j], dp[i][j + 1])
        
        return dp[0][0]    
        
                
sol=Solution()
#robot = [726554621,-235727278,-199823369]
#factory = [[612684362,1],[519972143,1],[759430060,2],[-76130291,1],[547454631,2],[47263647,2],[-79806151,2],[-329855292,0],[-954058831,3]]
robot = [-785116950,989862795,-894859426,-781626140,672589313,-941317336,989421436,174986851,-264848203,713675411,-244816575,-52030457,-371084440,-715835641,326827033,-931928762,-84629082,-308854322,-770052083,90773530]
factory=[[-964121556,20]]

print(sol.minimumTotalDistance(robot,factory))
print(sol.minimumTotalDistanceRigth(robot,factory))

