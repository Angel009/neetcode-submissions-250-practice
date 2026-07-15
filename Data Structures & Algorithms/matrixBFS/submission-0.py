class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        path_l = 0
        queue = deque()
        
        visit.add((0, 0))
        queue.append((0, 0))

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                if r == rows - 1 and c == cols - 1:
                    return path_l
                
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

                for dr, dc in directions:
                    if (min(r + dr, c + dc) < 0 or dr + r == rows or dc + c == cols or (r + dr, c + dc) in visit or grid[r + dr][c + dc] == 1):
                        continue
                    
                    visit.add((r + dr, c + dc))
                    queue.append((r + dr, c + dc))
                
            path_l += 1
        
        return -1