class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """
        My Answer: Time Limit Excceed

        if not prices:
            return 0
        
        profit = 0
        for i in range(len(prices)-1):
            tempMin = min(prices[:i+1])
            tempMax = max(prices[i+1:])
            if tempMin<tempMax:
                profit = max(profit,tempMax-tempMin)
        return profit
        """
        max_profit, min_price = 0, float('inf')

        for price in prices:
            min_price = min(min_price, price)

            profit = price - min_price

            max_profit = max(max_profit, profit)

        return max_profit