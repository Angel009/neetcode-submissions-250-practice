class Solution:
    def isPal(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        ans = []
        part = []
        
        def dfs(i):
            if i >= len(s):
                ans.append(part[:])
                return
            
            for j in range(i, len(s)):
                if self.isPal(s, i, j):
                    part.append(s[i:j + 1])
                    dfs(j + 1)
                    part.pop()
        
        dfs(0)
        return ans