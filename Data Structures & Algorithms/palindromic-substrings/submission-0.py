class Solution:
    def __init__ (self):
        self.ans = 0

    def palindrome_counts(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            self.ans += 1
            l -= 1
            r += 1
    
    def countSubstrings(self, s: str) -> int:
        for i in range(len(s)):
            self.palindrome_counts(s, i, i)
            self.palindrome_counts(s, i, i + 1)
        
        return self.ans