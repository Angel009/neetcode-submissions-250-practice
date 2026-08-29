class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0

        for i in range(len(digits)):
            curr = digits[i] * (10 ** (len(digits) - i - 1))
            num = num + curr
        
        ans = list(str(num + 1))

        return ans