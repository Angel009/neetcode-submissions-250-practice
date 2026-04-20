class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counter = {}
        s_counter = {}

        ans_indexes = [0, 0]
        ans_len = len(s) + 1

        if len(s) < len(t):
            return ""

        for c in t:
            t_counter[c] = 1 + t_counter.get(c, 0)
        
        left, have, need = 0, 0, len(t_counter)
        
        for right in range(len(s)):
            char = s[right]

            if char in t_counter:
                s_counter[char] = 1 + s_counter.get(char, 0)
            
            if char in t_counter and t_counter[char] == s_counter[char]:
                have += 1
            
            while need == have:
                if ans_len > (right - left + 1):
                    ans_len = (right - left + 1)
                    ans_indexes[0], ans_indexes[1] = left, right
                
                char_left = s[left]
                
                if char_left in s_counter:
                    s_counter[char_left] -= 1

                if char_left in t_counter and s_counter[char_left] < t_counter[char_left]:
                    have -= 1
                
                left += 1
            
        return s[ans_indexes[0]:ans_indexes[1] + 1] if ans_len != len(s) + 1 else ""
            