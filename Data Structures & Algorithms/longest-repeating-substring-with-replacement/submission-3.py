class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_letters = {}
        left = ans = max_l = 0

        for right in range(len(s)):
            count_letters[s[right]] = 1 + count_letters.get(s[right], 0)
            max_l = max(max_l, count_letters[s[right]])

            while (right - left + 1) - max_l > k:
                count_letters[s[left]] -= 1
                left += 1
            
            ans = max(ans, (right - left + 1))

        
        return ans