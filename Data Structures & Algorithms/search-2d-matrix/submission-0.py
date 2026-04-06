class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        set_matrix = set()
        for row in matrix:
            set_matrix.add(tuple(row))

        for elements in set_matrix:
            if target in elements:
                return True
        
        return False