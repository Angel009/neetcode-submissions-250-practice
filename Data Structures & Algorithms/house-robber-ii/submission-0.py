class Solution:
    def check_houses(self, nums):
        rob1 = rob2 = 0

        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2
    
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.check_houses(nums[1:]), self.check_houses(nums[:-1]))