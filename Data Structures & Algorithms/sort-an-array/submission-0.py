class Solution:

    def merge(self, x, y):
        ans = []
        i = j = 0

        while i < len(x) and j < len(y):
            if x[i] < y[j]:
                ans.append(x[i])
                i += 1
            else:
                ans.append(y[j])
                j += 1
        
        ans.extend(x[i:])
        ans.extend(y[j:])

        return ans

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        mid =  len(nums) // 2

        right = self.sortArray(nums[mid:])
        left = self.sortArray(nums[:mid])

        return self.merge(left, right)