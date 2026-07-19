class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        s =list(s)
        n = len(s)
        #q = deque()
        ans = 0
        count = 0
        for l in range(k):
            if s[l] in ('a', 'e', 'i', 'o', 'u'):
                count+=1
        ans = count
        #for i in range(k,n):
            #q.append(s[i])
            #new_arr = arr[i] + arr[i-k]
        for j in range(k, n):
            if s[j] in ('a', 'e', 'i', 'o', 'u'):
                count +=1
            if s[j-k] in ('a', 'e', 'i', 'o', 'u'):
                count -=1

            ans = max(ans,count)
        return ans
        