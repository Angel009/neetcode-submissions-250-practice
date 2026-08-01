class Solution:
    def rob(self, nums: List[int]) -> int:
        path_a = path_b = 0

        for n in nums:
            temp = max(n + path_a, path_b)
            path_a = path_b
            path_b = temp
        
        return path_b