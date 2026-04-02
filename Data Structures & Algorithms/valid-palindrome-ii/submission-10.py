class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                m_left = s[left + 1: right + 1]
                m_right = s[left:right]

                return m_left == m_left[::-1] or m_right == m_right[::-1]
            
            left += 1
            right -= 1
        
        return True