class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        if len(strs) == 0:
            return [strs]
        
        group = {}
        ans = []

        for chars in strs:
            char_value = "".join(sorted(chars))


            if char_value not in group:
                group[char_value] = [chars]
            else:
                group[char_value].append(chars)
        
        for v in group.values():
            ans.append(v)
        
        return ans