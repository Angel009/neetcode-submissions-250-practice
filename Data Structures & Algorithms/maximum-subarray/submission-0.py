class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]
        ans = nums[0]
        
        for right in range(1, len(nums)):
            curr = max(nums[right], curr + nums[right])
            
            ans = max(ans, curr)
        
        return ans