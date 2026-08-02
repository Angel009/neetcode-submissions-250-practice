class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        ans_index = ans_len = 0

        def pal_helper(l, r):
            nonlocal ans_index, ans_len
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > ans_len:
                    ans_index = l
                    ans_len = r - l + 1
                
                l -= 1
                r += 1

        for i in range(len(s)):
            pal_helper(i, i)
            pal_helper(i, i + 1)
        
        return s[ans_index:ans_index + ans_len]
