class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(map(int, str(num)))
        n=len(s)
        if n==1:
            return num
        elif n==2:
            if s[0]<s[1]:
                s[0],s[1]=s[1],s[0]
                return int(''.join(map(str,s)))
            else:
                return num                
        else:
            arr=[(-1,-1)]*n
            for i in range(n-2,-1,-1):
                arr[i]=max(arr[i+1],(s[i+1],i+1))
            for i in range(n):
                val=s[i]
                if arr[i][0]>val:
                    s[i],s[arr[i][1]]=s[arr[i][1]],s[i]
                    return int(''.join(map(str,s)))
            return num
               

sol=Solution()
print(sol.maximumSwap(98368))