class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows_zero = set()
        cols_zero = set()

        rows = len(matrix)
        cols = len(matrix[0])

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    rows_zero.add(r)
                    cols_zero.add(c)
        
        for r in range(rows):
            for c in range(cols):
                if r in rows_zero or c in cols_zero:
                    matrix[r][c] = 0
        