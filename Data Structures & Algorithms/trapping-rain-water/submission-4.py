class Solution:
    def trap(self, height: list[int]) -> int:
        if len(height) == 1:
            return 0
        
        max_left = []
        max_right = []
        minimum_left_right = []

        for h in range(len(height)):
            left, right = height[: h], height[h + 1:]

            if len(left) > 0 and len(right) > 0:
                max_left.append(max(left))
                max_right.append(max(right))
            elif len(left) == 0:
                max_left.append(0)
                max_right.append(max(right))
            elif len(right) == 0:
                max_left.append(max(left))
                max_right.append(0)
            else:
                return 0

        for i in range(len(max_left)):
            minimum_left_right.append(min(max_left[i], max_right[i]))

        total_rain = 0
        for h in range(len(height)):
            sum = minimum_left_right[h] - height[h]
            if sum >= 0:
                total_rain += sum

        return total_rain

            