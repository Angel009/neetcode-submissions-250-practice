class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        left = 0
        max_num = 0

        for right in range(len(nums)):
            max_num = max(max_num, nums[right])

            if (right - left + 1) == k:
                max_num = max(nums[left:right + 1])
                ans.append(max_num)
                left += 1
            
        
        return ans