class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        notepad='A'
        i=0
        copyAll=None
        count=0
        while i<n:
            if len(notepad)==n:
                break
            else:
                if n%len(notepad)==0:
                    copyAll=notepad
                    count+=1
                notepad=notepad+copyAll
                count+=1
            i+=1
        return count
    
sol=Solution()
print(sol.minSteps(10))
            
