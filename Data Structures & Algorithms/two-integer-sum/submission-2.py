class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            new_target = target - nums[i]
            for l in range(i + 1, len(nums)):
                if new_target == nums[l]:
                    return [i, l]
        