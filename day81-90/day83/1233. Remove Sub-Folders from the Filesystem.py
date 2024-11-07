from typing import List

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        ans = [folder[0]]
        for i in range(1, len(folder)):
            if folder[i].startswith(ans[-1] + "/") :
                continue
            ans.append(folder[i])
        return ans
    

sol=Solution()
folder =["/a","/a/b","/c/d","/c/d/e","/c/f","/a","/a/b"]
print(sol.removeSubfolders(folder))