class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        for i in s1:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1

        size_of_window = len(s1)

        for l in range(0, 1 + len(s2) - size_of_window):
            new = s2[l: l + size_of_window]
            new_count = {}
            for k in new:
                if k not in new_count:
                    new_count[k] = 1
                else:
                    new_count[k] += 1

            if new_count == count:
                return True

        return False