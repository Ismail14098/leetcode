class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 0
        result = 0
        while r < len(prices):
            result = max(prices[r]-prices[l], result)
            if prices[r] < prices[l]:
                l = r
            r += 1
        return result