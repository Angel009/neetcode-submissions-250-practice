class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_s = set()
        left = 0
        ans = 0

        for right in range(len(s)):
            while s[right] in sub_s:
                sub_s.remove(s[left])
                left += 1
            
            sub_s.add(s[right])
            ans = max(ans, right - left + 1)
        
        return ans