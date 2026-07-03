class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        perms = []
        counter = {}

        for n in nums:
            counter[n] = counter.get(n, 0)
        
        for n in nums:
            counter[n] += 1
        
        def dfs():
            if len(perms) == len(nums):
                ans.append(perms[:])
                return
            
            for n in counter:
                if counter[n] > 0:
                    perms.append(n)
                    counter[n] -= 1

                    dfs()

                    counter[n] += 1
                    perms.pop()
        
        dfs()

        return ans