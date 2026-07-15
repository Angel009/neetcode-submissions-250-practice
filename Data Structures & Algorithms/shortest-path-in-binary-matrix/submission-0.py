class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
            return -1

        visit = set()
        queue = deque()
        path_l = 1

        visit.add((0, 0))
        queue.append((0, 0))

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                if r == rows - 1 and c == cols - 1:
                    return path_l
                
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, 1], [1, -1], [-1, -1]]

                for dr, dc in directions:
                    if (min(dr + r, dc + c) < 0 or dr + r == rows or dc + c == cols or (r + dr, c + dc) in visit or grid[r + dr][c + dc] == 1):
                        continue
                    
                    visit.add((dr + r, dc + c))
                    queue.append((dr + r, dc + c))
            
            path_l += 1
        
        return -1