class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        for  i in range(n):
            nums[i+n] |= nums[i] << 10

        j = 0
        for i in range(n, 2*n):
            x = nums[i] >> 10
            y = nums[i] & 1023
            nums[j] = x
            nums[j+1] = y
            j+=2
        return nums




        