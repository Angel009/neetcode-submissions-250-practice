class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        max_range = 0
        curr_l = 0

        for i in range(len(nums) - 1):
            max_range = max(max_range, i + nums[i])

            if i == curr_l:
                jumps += 1
                curr_l = max_range
        
        return jumps