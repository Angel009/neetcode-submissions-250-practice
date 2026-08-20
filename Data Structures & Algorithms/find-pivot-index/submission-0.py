class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [0]

        for i in range(len(nums)):
            prefix.append(prefix[-1] + nums[i])
        
        for i in range(1, len(prefix)):
            if (prefix[-1] - prefix[i]) == prefix[i - 1]:
                return i - 1
        
        return -1