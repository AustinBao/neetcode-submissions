class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target == nums[0]:
            return 0    

        left = 0
        right = len(nums)

        while left + 1 != right:
            middle = (left + right) // 2
            if target == nums[middle]:
                return middle
            elif target > nums[middle]:
                left = middle
            elif target < nums[middle]:
                right = middle

        return -1