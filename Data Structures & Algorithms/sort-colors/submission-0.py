class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroes = ones = 0
        twos = len(nums) - 1

        while ones <= twos:
            if nums[ones] == 0:
                nums[ones], nums[zeroes] = nums[zeroes], nums[ones]
                ones += 1
                zeroes += 1
            elif nums[ones] == 1:
                ones += 1
            else:
                nums[ones], nums[twos] = nums[twos], nums[ones]
                twos -= 1

        