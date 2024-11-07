class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False

        frequency_chars_s1=[0]*26
        window=[0]*26
        for i in range(len(s1)):
            frequency_chars_s1[ord(s1[i])-ord('a')]+=1
            window[ord(s2[i])-ord('a')]+=1
        for i in range(len(s1),len(s2)):
            if frequency_chars_s1==window:
                return True
            window[ord(s2[i])-ord('a')]+=1
            window[ord(s2[i-len(s1)])-ord('a')]-=1
            
        return frequency_chars_s1==window
            
        
sol=Solution()
s1="ab"
s2="eidboaoo"
print(sol.checkInclusion(s1,s2))

    
        
