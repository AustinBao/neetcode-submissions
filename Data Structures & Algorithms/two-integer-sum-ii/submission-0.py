class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            new_target = target - numbers[i]
            for l in range(i + 1, len(numbers)):
                if new_target == numbers[l]:
                    return [i + 1, l + 1]