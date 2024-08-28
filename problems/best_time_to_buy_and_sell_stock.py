class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = prices[0]
        profit = 0
        for i in prices[0:]:
            if i < buy:
                buy = i
            elif i - buy > profit:
                profit = i - buy
        
        return profit

sol = Solution()

prices = [2, 4, 1]

res = sol.maxProfit(prices)
print(res)