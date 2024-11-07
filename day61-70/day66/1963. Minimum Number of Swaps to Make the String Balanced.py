class Solution:
    def minSwaps(self, s: str) -> int:
        store={"open":0,"close":0}
        count=0
        for char in s:
            if store["open"]==len(s)//2:
                break
            if char=="[":
                store["open"]+=1
            elif char=="]":
                store["close"]+=1
            if store["close"]>store["open"]:
                store["close"]-=1
                store["open"]+=1
                count+=1
        return count

    def minSwaps2(self, s: str) -> int:
        # cuenta la cantidad de "]"" no balanceados
        count_closed = 0
        # almacena "["
        stack=[]
        for char in s:
            if char=="[":
                stack.append(char)
            else:
                if stack:
                    stack.pop()
                else:
                    count_closed+=1
        
        return (count_closed+1)//2
    

sol=Solution()
s = "][][[][]["
print(sol.minSwaps2(s))
        