class Solution(object):
    def chalkReplacer(self, chalk, k):
        """
        :type chalk: List[int]
        :type k: int
        :rtype: int
        """
        n=len(chalk)
        i=0
        sumaChalk=sum(chalk)
        residuo=k%sumaChalk
        while residuo>=chalk[i]:
            residuo-=chalk[i]
            i=(i+1)%n
        return i
    
chalk = [8,66,38,1,9,84,35,56,20,50,89,21,72,8,1,9,86,75,99,90,25,87,72,1,33,64,10,37,80,21,60,56,10,77,32,37,72,72,88,18,11,44,21,75,100,77,57,50,74,32,72,25,8,41,34,93,74,19,46,21,90,57,88,98,29,63,52,74,27,4,63,94,3,19,69,16,26,11,22,52,5,17,40,86,96,29]
k = 661513648
s=Solution()

print(s.chalkReplacer(chalk,k))