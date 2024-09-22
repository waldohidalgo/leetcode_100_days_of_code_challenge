import re

class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        def transformTimetoMinutes(hour):
            pattern=r"(\d+):(\d+)"
            return int(re.findall(pattern,hour)[0][0])*60+int(re.findall(pattern,hour)[0][1])
        
        times=[transformTimetoMinutes(x) for x in timePoints]
        times.sort()
        minDistance=float('inf')
        for i in range(1,len(times)):
            minDistance=min(minDistance,times[i]-times[i-1])
        minDistance=min(minDistance,24*60-(times[-1]-times[0]))
        return minDistance
    
sol=Solution()
timePoints=["00:00","23:59","00:00"]

print(sol.findMinDifference(timePoints))