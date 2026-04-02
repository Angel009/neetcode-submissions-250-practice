class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        frequency = {}
        arr, ans = [], []
        len_nums = len(nums)

        for num in nums:
            frequency[num] = 1 + frequency.get(num, 0)
        
        for key, val in frequency.items():
            arr.append([val, key])
        
        arr.sort(reverse = True)

        for element in arr:
            if element[0] > len_nums // 3:
                ans.append(element[1])
        
        return ans
        