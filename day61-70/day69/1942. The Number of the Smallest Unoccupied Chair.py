from typing import List
import heapq
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)

        events = []

        for i, (arrive, leave) in enumerate(times):
            events.append((arrive, 'arrive', i))  
            events.append((leave, 'leave', i))    
 
        events.sort(key=lambda x: (x[0], x[1] == 'arrive'))
        
        free_chairs = []

        chair_assigned = [-1] * n

        next_chair = 0

        for _, event_type, friend in events:
            if event_type == 'arrive':
                
                if free_chairs:
                    assigned_chair = heapq.heappop(free_chairs)  
                else:
                    assigned_chair = next_chair  
                    next_chair += 1
                
                chair_assigned[friend] = assigned_chair
                
                if friend == targetFriend:
                    return assigned_chair
            
            elif event_type == 'leave':
                
                heapq.heappush(free_chairs, chair_assigned[friend])
            
sol=Solution()

times = [[3,10],[1,5],[2,6]]
targetFriend = 0
print(sol.smallestChair(times, targetFriend))
            

                