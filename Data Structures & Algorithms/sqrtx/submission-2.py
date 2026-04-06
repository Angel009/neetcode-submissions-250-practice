class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        l, r = 1, x

        while l <= r:
            sqrt_n = (l + r) // 2
            total = int(sqrt_n * sqrt_n)

            if total == x:
                return sqrt_n
            elif total < x:
                l = sqrt_n + 1
            elif total > x:
                r = sqrt_n - 1
        
        return r
        
            