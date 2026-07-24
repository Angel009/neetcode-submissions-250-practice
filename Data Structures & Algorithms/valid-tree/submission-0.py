class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        
        adj = {i:[] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visit = set()

        def dfs(curr, prev):
            if curr in visit:
                return False
            
            visit.add(curr)

            for i in adj[curr]:
                if i == prev:
                    continue
                
                if not dfs(i, curr):
                    return False
            return True
        
        return dfs(0, -1) and n == len(visit)