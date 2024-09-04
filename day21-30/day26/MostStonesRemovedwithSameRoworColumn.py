class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        nodes=[[] for _ in range(len(stones))]
        for i in range(len(stones)):
            for j in range(i+1,len(stones)):
                if stones[i][0]==stones[j][0] or stones[i][1]==stones[j][1]:
                    nodes[i].append(j)
                    nodes[j].append(i)
        visited=set()
        def dfs(i):
            for j in nodes[i]:
                if j not in visited:
                    visited.add(j)
                    dfs(j)
        count=0
        for i in range(len(stones)):
            if i not in visited:
                dfs(i)
                count+=1
        return len(stones)-count
        
sol=Solution()
print(sol.removeStones([[0,0],[0,2],[1,1],[2,0],[2,2]]))