class Solution:
    def isPalindrome(self, s: str) -> bool:
        abc = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
        s = s.upper()
        pal_s = []
        
        for c in s:
            if c in abc:
                pal_s.append(c)
        
        left = 0
        right = len(pal_s) - 1

        while left < right:
            if pal_s[left] != pal_s[right]:
                return False
            left += 1
            right -= 1
        
        return True
