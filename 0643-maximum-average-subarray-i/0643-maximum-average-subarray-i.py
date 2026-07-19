class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        max_ans = sum(nums[:k])
        ans = max_ans
        for i in range(k,n):
            #ans = max_ans + nums[i+1] - nums[i-k]
            ans+= nums[i] - nums[i-k] 
            max_ans = max(max_ans, ans)
        return max_ans/k
        
