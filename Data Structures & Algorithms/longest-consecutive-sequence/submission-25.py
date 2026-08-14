class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        
        longest = 0
        for num in nums:
            curr_len = 1                
            if num - 1 not in nums:
                while num + 1 in nums:
                    curr_len += 1
                    num += 1
            longest = max(longest, curr_len)
        return longest