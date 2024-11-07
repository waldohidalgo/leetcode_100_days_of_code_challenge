class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        maxLength=1
        def backtrack(i, seen):
            nonlocal maxLength
            if i == len(s):
                maxLength = max(maxLength, len(seen))
                return
            for j in range(i+1, len(s)+1):
                if s[i:j] in seen:
                    continue
                seen.add(s[i:j])
                backtrack(j, seen)
                seen.remove(s[i:j])
        
        backtrack(0, seen=set())
        return maxLength
sol=Solution()
print(sol.maxUniqueSplit("aa"))