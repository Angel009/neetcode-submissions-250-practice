class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_map = {i:[] for i in range(numCourses)}

        for c, p in prerequisites:
            pre_map[c].append(p)
        
        visit = set()

        def dfs(crs):
            if crs in visit:
                return False
            if pre_map[crs] == []:
                return True
            
            visit.add(crs)

            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False
            
            visit.remove(crs)
            pre_map[crs] = []

            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True