class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        size = 0
        l = 0
        for r in range(len(s)):
            if s[r] not in count:
                count[s[r]] = 1
            else:
                count[s[r]] += 1

            if size - max(count.values()) < k:
                size += 1
            else:
                count[s[l]] -= 1
                l += 1

        return size