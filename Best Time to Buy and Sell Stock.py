class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        low = sys.maxsize
        for i in prices:
            if (i < low):
                low = i
            if (i - low > profit):
                profit = i - low

        return profit
