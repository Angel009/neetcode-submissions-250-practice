class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if not nums or len(nums) <= 2:
            return True
        
        decrease = False
        increase = False

        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                decrease = True
            elif nums[i - 1] < nums[i]:
                increase = True
            
            if decrease and increase:
                return False
        
        return True

        