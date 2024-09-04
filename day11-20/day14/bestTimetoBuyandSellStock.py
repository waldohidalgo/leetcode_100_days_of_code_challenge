class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit=0
        minPrice=float('inf')

        for price in prices:
            if price<minPrice:
                minPrice=price
            elif price-minPrice>maxProfit:
                maxProfit=price-minPrice
        return maxProfit
    
sol=Solution()
print(sol.maxProfit([2,4,1]))