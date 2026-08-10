class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = False
        for number in nums:
            copy = nums.copy()
            copy.remove(number)
            if number in copy:
                duplicate = True

        return duplicate