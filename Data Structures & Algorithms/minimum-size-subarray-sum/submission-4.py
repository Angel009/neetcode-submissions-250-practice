class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        num_sum = 0
        left = 0
        ans = len(nums) + 1

        for right in range(len(nums)):
            num_sum += nums[right]

            while num_sum >= target:
                ans = min(ans, right - left + 1)
                num_sum -= nums[left]
                left += 1
            
        return 0 if ans == len(nums) + 1 and num_sum < target else ans