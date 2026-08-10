class Solution:
    def maxArea(self, heights: List[int]) -> int:
        areas = []
        l, r = 0, len(heights) - 1

        while l != r:
            if heights[l] > heights[r]:
                areas.append(heights[r] * (r - l))
                r -= 1
            else:
                areas.append(heights[l] * (r - l))
                l += 1

        return max(areas)