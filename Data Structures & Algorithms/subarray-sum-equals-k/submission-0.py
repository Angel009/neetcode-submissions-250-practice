class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = {0:1}
        ans = curr = 0

        for num in nums:
            curr += num

            if curr - k in counts:
                ans += counts[curr - k]
            
            counts[curr] = 1 + counts.get(curr, 0)
        
        return ans
        