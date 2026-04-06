class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        ans = right

        while left <= right:
            k = (left + right) // 2
            curr_h = 0

            for pile in piles:
                curr_h += math.ceil(pile / k)

            if curr_h <= h:
                ans = min(ans, k)
                right = k - 1
            else:
                left = k + 1
        
        return ans