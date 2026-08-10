class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = heights[0]
        stack = []
        for i, h in enumerate(heights):
            startIndex = i
            while len(stack) != 0 and stack[-1][1] > h:
                popped_index, popped_height = stack.pop()
                maxArea = max(maxArea, popped_height * (i - popped_index))
                startIndex = popped_index
            stack.append((startIndex, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea

