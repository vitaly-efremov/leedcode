from typing import List


class SimpleSolution:
    def maxArea(self, height: List[int]) -> int:
        bars_count = len(height)
        if bars_count == 2:
            return min(height)

        max_area = 0
        for start_index in range(0, bars_count - 1):
            for end_index in range(start_index + 1, bars_count):
                width = end_index - start_index
                min_height = min(height[start_index], height[end_index])
                current_area = min_height * width
                if current_area > max_area:
                    max_area = current_area

        return max_area


class Solution:
    def maxArea(self, height: List[int]) -> int:
        bars_count = len(height)
        if bars_count == 2:
            return min(height)

        max_area = 0
        start_index = 0
        end_index = bars_count - 1
        while start_index <= end_index:
            width = end_index - start_index
            if height[start_index] < height[end_index]:
                area = height[start_index] * width
                start_index += 1
            else:
                area = height[end_index] * width
                end_index -= 1

            max_area = max(area, max_area)

        return max_area


if __name__ == '__main__':
    solution = Solution()
    assert solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert solution.maxArea([1, 1]) == 1

    print('All good!')
