class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for t in range(len(temperatures)):
            count = 1
            for d in range(t + 1, len(temperatures)):
                if temperatures[d] > temperatures[t]:
                    res.append(count)
                    break
                elif d == len(temperatures) - 1:
                    res.append(0)
                    break
                count += 1

        res.append(0)

        return res
        