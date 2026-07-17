class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s = list(s)
        n = len(s)
        i = 0
        j = n-1
        while i<j:
            if s[i] == s[j]:
                i+=1
                j-=1

            elif s[i]>s[j]:
                s[i] = s[j]
                i+=1
                j-=1
            else:
                s[j] = s[i]
                i+=1
                j-=1

        return "".join(s)

