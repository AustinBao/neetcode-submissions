class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final = []
        for i, _ in enumerate(nums):
            product = 1
            for j, number in enumerate(nums):
                if j != i:
                    product *= number
            final.append(product)

        return final