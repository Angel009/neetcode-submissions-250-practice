class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) == 0:
            return [[]]
        
        ans = []
        perms = self.permute(nums[1:])

        for p in perms:
            for i in range(len(p) + 1):
                curr = p[:]
                curr.insert(i, nums[0])
                ans.append(curr)
        
        return ans
        