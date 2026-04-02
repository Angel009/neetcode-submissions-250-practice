class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        len_nums = len(nums)

        for i in range(len_nums):
            while val in nums:
                nums.remove(val)

        return len(nums)