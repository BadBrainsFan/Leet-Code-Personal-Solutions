class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0,1
        maximum_profit = 0
        while right < len(prices):
            if prices[right] > prices[left]:
                current_profit = prices[right] - prices[left]
                maximum_profit = max(maximum_profit, current_profit)
            else:
                left = right
            right += 1
        return maximum_profit