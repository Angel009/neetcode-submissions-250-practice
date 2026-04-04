# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        min_n = 1
        max_n = n

        mid_n = (max_n - min_n) // 2
        guess_res = guess(mid_n)
        
        while guess_res != 0:
            mid_n = (min_n + max_n) // 2
            guess_res = guess(mid_n)

            if guess_res == - 1:
                max_n = mid_n - 1
            elif guess_res == 1:
                min_n = mid_n + 1
            else:
                return mid_n
        
        return mid_n

        