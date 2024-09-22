class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        reversed_string = s[::-1]  

        palindrome=""
        for i in range(length):
            if s[: length - i] == reversed_string[i:]:
                palindrome= reversed_string[:i] + s
                break
        return palindrome
                
sol=Solution()
print(sol.shortestPalindrome("aacecaaa"))



            
            
