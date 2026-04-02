class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequency = {}

        for c in s:
            if c not in frequency:
                frequency[c] = 1
            else:
                frequency[c] += 1
        
        for c in t:
            if c not in frequency:
                return False
            else:
                frequency[c] -= 1
        
        for v in frequency.values():
            if v != 0:
                return False
        
        return True