class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_l = [nums[0]]
        prefix_r = [nums[len(nums) - 1]]

        ans = []

        for i in range(1, len(nums)):
            prefix_l.append(nums[i] * prefix_l[-1])
        
        for i in range(len(nums) - 2, -1, -1):
            prefix_r.append(nums[i] * prefix_r[-1])
        
        prefix_r = prefix_r[::-1]

        for i in range(len(nums)):
            if i == 0:
                ans.append(prefix_r[i + 1])
            elif i == len(nums) - 1:
                ans.append(prefix_l[i - 1])
            else:
                ans.append(prefix_l[ i - 1] * prefix_r[i + 1])
        
        return ans