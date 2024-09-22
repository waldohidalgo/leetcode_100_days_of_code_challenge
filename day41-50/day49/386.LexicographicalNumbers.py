class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result=[]
        num=1
        for _ in range(n):
            result.append(num)
            if num*10<=n:
                num*=10
            elif num%10!=9 and num+1<=n:
                num+=1
            else:
                num=(num//10)
                num+=1
                # este bucle vuelve a la primera cifra
                while num%10==0:
                    num//=10
        return result
    
# sol=Solution()
# print(sol.lexicalOrder(1005))


from functools import cmp_to_key

def compare(x,y):
    x=str(x)
    y=str(y)
    if x<y:
        return -1
    elif x>y:
        return 1
    else:
        return 0
    
arr=list(range(1,15))
arr.sort(key=cmp_to_key(compare))
print(arr)