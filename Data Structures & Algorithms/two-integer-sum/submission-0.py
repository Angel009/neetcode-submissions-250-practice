class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        operations = {}

        for index, num in enumerate(nums):
            if target - num not in operations:
                operations[num] = index
            else:
                return [operations[target - num], index]