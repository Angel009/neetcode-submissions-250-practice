class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        uniques = set()

        for num in nums:
            if num in uniques:
                return num
            else:
                uniques.add(num)