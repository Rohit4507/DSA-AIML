class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        for i in arr:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] +=1

        seen =set()

        for count in freq.values():
            if count in seen:
                return False
            else:
                seen.add(count)

        return True


