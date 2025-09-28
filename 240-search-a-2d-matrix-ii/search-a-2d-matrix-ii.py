class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix[0])
        n = len(matrix)
        row = 0
        col = m-1
        while(row< n and col >= 0):
            if matrix[row][col] == target:
                return row,col
            elif matrix[row][col] < target:
                row = row +1
            else:
                col = col - 1
        return False
        