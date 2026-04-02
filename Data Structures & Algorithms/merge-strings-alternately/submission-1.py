class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len_w1 = len(word1)
        len_w2 = len(word2)

        merged_str = []

        if len_w1 > len_w2:
            for i in range(len_w2):
                merged_str.append(word1[i] + word2[i])
            merged_str.append(word1[i + 1:])
        else:
            for i in range(len_w1):
                merged_str.append(word1[i] + word2[i])
            merged_str.append(word2[i + 1:])
        
        return "".join(merged_str)