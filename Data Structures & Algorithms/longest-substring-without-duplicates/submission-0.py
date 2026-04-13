class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = ans = 0
        chars_pos = {}

        for right in range(len(s)):
            if s[right] in chars_pos:
                left = max(left, chars_pos[s[right]])
            
            ans = max(ans, right - left + 1)

            chars_pos[s[right]] = right + 1
        
        return ans