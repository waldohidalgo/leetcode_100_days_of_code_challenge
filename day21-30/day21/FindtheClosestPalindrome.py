class Solution:
    def nearestPalindromic(self, n: str) -> str:
        largo=len(n)
        firstHalf=n[:(largo+1)//2]
        possibilities=[]

        if largo%2==0:
            possibility=firstHalf+firstHalf[::-1]
            if possibility!=n:
                possibilities.append(possibility)
        else:
            possibility=firstHalf+firstHalf[::-1][1:]
            if possibility!=n:
                possibilities.append(possibility)

        firstHalfPlusOne=str(int(firstHalf)+1)
        if largo%2==0:
            possibility=firstHalfPlusOne+firstHalfPlusOne[::-1]
            if possibility!=n:
                possibilities.append(possibility)
        else:
            possibility=firstHalfPlusOne+firstHalfPlusOne[::-1][1:]
            if possibility!=n:
                possibilities.append(possibility)
            
        firstHalfMinusOne=str(int(firstHalf)-1)
        if largo%2==0:
            possibility=firstHalfMinusOne+firstHalfMinusOne[::-1]
            if possibility!=n:
                possibilities.append(possibility)
        else:
            possibility=firstHalfMinusOne+firstHalfMinusOne[::-1][1:]
            if possibility!=n:
                possibilities.append(possibility)
        possibilities.append(str(10**(largo-1)-1))
        possibilities.append(str(10**(largo)+1))
        print(possibilities)
        diff=float('inf')
        res=0
        for possibility in possibilities:
            if abs(int(n)-int(possibility))<diff:
                diff=abs(int(n)-int(possibility))
                res=int(possibility)
            elif abs(int(n)-int(possibility))==diff:
                res=min(res,int(possibility))
        return str(res)
    
sol=Solution()
print(sol.nearestPalindromic("999"))
        
        

       
            