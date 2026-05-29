class Solution:
    def romanToInt(self, s: str) -> int:
        roman_int = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        total = 0
        curr = 0

        for i in range(len(s) - 1, -1, -1):
            c = roman_int[s[i]]
            if c >= curr:
                total += c
            else:
                total -= c
            
            curr = c
        
        return total