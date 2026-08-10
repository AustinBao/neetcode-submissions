class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        final = []
        for i in range(len(nums) - k + 1):
            curr = nums[i: i + k]
            final.append(max(curr))
            
        return final