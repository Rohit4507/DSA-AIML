class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        grid = [val for i in grid for val in i]
        arr1 = []
        n = len(grid)
        arr2 = list(range(1, n + 1))
        grid.sort()
        for i in range(n-1):
            if grid[i] == grid[i+1]:
                arr1.append(grid[i])
        for num in arr2:
            if num not in grid:
                arr1.append(num)
                break

        return arr1
        