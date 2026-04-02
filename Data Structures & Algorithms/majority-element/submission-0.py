class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}

        for num in nums:
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1
        
        max_val = curr_val = 0

        for key, val in counter.items():
            curr_val = max(curr_val, val)

            if val == curr_val:
                max_val = key
        
        return max_val
        