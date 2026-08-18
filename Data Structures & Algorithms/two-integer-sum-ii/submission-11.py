class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        for _ in range(len(numbers)):
            find = target - numbers[l]
            
            if find == numbers[r]:
                return[l + 1, r + 1]

            elif find > numbers[r]:
                l += 1
            
            elif find < numbers[r]:
                r -= 1




