class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """
        My Answer: Not Right

        if not prices:
            return 0
        buy = 0
        sell = 0
        profit = 0
        i=0
        for i in xrange(1,len(prices)):
            if prices[i]<prices[sell]:
                profit += (prices[sell]-prices[buy])
                buy = i
                sell = i
            else:
                if (prices[i]-prices[buy])>(prices[sell]-prices[buy]):
                    sell = i
        if i==sell:
            profit += (prices[sell]-prices[buy])
        return profit
        """
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))