class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = {}
        for integer in nums:
            if integer not in count:
                count[integer] = 1
            else:
                count[integer] += 1
                if count[integer] > 1:
                    return integer
        

        