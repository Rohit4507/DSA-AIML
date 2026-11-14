class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        flat_arr = [num for row in grid for num in row]
        nums = flat_arr
        arr1 = []
        n = len(nums)
        arr2 = list(range(1, n + 1))
        nums.sort()
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                arr1.append(nums[i])
        for num in arr2:
            if num not in nums:
                arr1.append(num)
                break

        return arr1
        