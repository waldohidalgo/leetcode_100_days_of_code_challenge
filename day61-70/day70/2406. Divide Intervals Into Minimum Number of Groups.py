from typing import List
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        events=[]
        for s,e in intervals:
            events.append([s,"in"])
            events.append([e,"out"])
        events.sort(key=lambda x:(x[0],x[1]=="out"))
        overlap_count=0
        max_overlap=0
        for _,event in events:
            if event=="in":
                overlap_count+=1
                max_overlap=max(max_overlap,overlap_count)
            else:
                overlap_count-=1
        return max_overlap
    
    
        
    
sol=Solution()
intervals=[[5,10],[6,8],[1,5],[2,3],[1,10]]
print(sol.minGroups2(intervals))
        