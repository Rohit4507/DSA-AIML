class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        threshold = len(nums)//2
        frequencies: dict[int, int] = {}
        for value in nums:
            frequencies[value] = frequencies.get(value, 0)+1
            if frequencies[value] > threshold:
                return value

        return -1