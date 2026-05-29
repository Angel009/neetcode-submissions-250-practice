class Solution:
    def isHappy(self, n: int) -> bool:
        unique = set()

        while True:
            n_str = str(n)
            total = 0

            for c in n_str:
                total = total + int(c) ** 2
            
            if total in unique:
                return False
            
            if total == 1:
                return True
            
            unique.add(total)
            n = total

        