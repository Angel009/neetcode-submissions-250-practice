class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or not strs[0]:
            return ""
            
        lcp = strs[0]

        for chars in strs:
            while not chars.startswith(lcp):
                lcp = lcp[:-1]
                if not lcp:
                    return ""
        
        return lcp
