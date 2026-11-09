class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        original = [row[:] for row in matrix]
        for row in range(rows):
            for col in range(cols):
                if original[row][col] == 0:
                    for i in range(cols):
                        matrix[row][i] = 0
                    for j in range(rows):
                        matrix[j][col] = 0
                