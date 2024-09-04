class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"

        below_20 = ['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven',
                    'Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
        tens = ['','Ten','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']

        def helper(n):
            if n == 0:
                return ''
            elif n < 20:
                return below_20[n] + ' '
            elif n < 100:
                return tens[n // 10] + ' ' + helper(n % 10)
            else:
                return below_20[n // 100] + ' Hundred ' + helper(n % 100)

        res = ''
        
        while num > 0:
            if num>=1000000000:
                res += helper(num // 1000000000) + 'Billion '
                num = num % 1000000000

            if num>=1000000:
                res += helper(num // 1000000) + 'Million '
                num = num % 1000000

            if num>=1000:
                res += helper(num // 1000) + 'Thousand '
                num = num % 1000
            
            if num>=100:
                res += helper(num // 100) + 'Hundred '
                num = num % 100
            if num>0:
                res += helper(num)
                num = 0

        return res.strip()
    


sol=Solution()
print(sol.numberToWords(1234567))