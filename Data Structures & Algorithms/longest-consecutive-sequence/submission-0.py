class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_len = 0

        for num in nums:
            len_n = 1
            next_n = num + 1

            while next_n in nums:
                next_n += 1
                len_n += 1
            
            max_len = max(max_len, len_n)
        
        return max_len