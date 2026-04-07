class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        ans = right

        def ship(cap):
            ships, curr_cap = 1, cap

            for w in weights:
                if curr_cap - w < 0:
                    ships += 1
                    curr_cap = cap
                curr_cap -= w
            return ships <= days
        
        while left <= right:
            m = (left + right) // 2

            if ship(m):
                ans = min(ans, m)
                right = m - 1
            else:
                left = m + 1
        
        return ans