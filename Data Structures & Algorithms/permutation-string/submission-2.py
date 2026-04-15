class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1_l = len(s1)
        n2_l = len(s2)

        if n1_l > n2_l:
            return False
        
        s1_counts = [0] * 26
        s2_counts = [0] * 26

        for i in range(len(s1)):
            s1_counts[ord(s1[i]) - ord("a")] += 1
            s2_counts[ord(s2[i]) - ord("a")] += 1
        
        if s1_counts == s2_counts:
            return True
        
        for i in range(n1_l, n2_l):
            s2_counts[ord(s2[i]) - ord("a")] += 1
            s2_counts[ord(s2[i - n1_l]) - ord("a")] -= 1

            if s1_counts == s2_counts:
                return True
        
        return False