class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold, held, reset = -math.inf, -math.inf, 0

        for i in range(len(prices)):
            prevSold = sold
            sold = held + prices[i]
            held = max(held, reset - prices[i])
            reset = max(reset, prevSold)
        
        return max(sold, reset)
