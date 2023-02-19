# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1,
# return the area of the largest rectangle in the histogram.  Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.Constraints:
#
#  constraints
# 1 <= heights.length <= 105
# 0 <= heights[i] <= 104
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        left_limit = [0] * len(heights)
        right_limit = [0] * len(heights)
        stack = []

        for i in range(len(heights)):
            if not stack:
                left_limit[i] = 0
            else:
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                top = stack[-1] + 1 if stack else 0
                left_limit[i] = top
            stack.append(i)
        stack = []

        for i in range(len(heights) - 1, -1, -1):
            if not stack:
                right_limit[i] = len(heights) - 1
            else:
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                top = stack[-1] - 1 if stack else len(heights) - 1
                right_limit[i] = top
            stack.append(i)
        max_area = 0
        for i in range(len(heights)):
            area = (right_limit[i] - left_limit[i] + 1) * heights[i]
            max_area = max(area, max_area)
        return max_area
