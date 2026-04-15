class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, curr_sum = 0, 0
        ans = len(nums) + 1
        
        for right in range(len(nums)):
            curr_sum += nums[right]

            while curr_sum >= target:
                ans = min(ans, right - left + 1)
                curr_sum -= nums[left]
                left += 1
        
        return ans if ans != len(nums) + 1 else 0