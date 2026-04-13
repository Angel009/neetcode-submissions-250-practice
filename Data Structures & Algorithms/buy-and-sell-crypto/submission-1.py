class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prev = 0
        ans = 0

        for right in range(1, len(prices)):
            while prices[right] < prices[prev]:
                prev += 1
            
            if prices[right] > prices[prev]:
                ans = max(ans, prices[right] - prices[prev])
        
        return ans