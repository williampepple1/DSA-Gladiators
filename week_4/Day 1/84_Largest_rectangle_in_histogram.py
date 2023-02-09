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
        leftlimit = [0]*len(heights)
        rightlimit = [0]*len(heights)
        stack = []

        for i in range(len(heights)):
            if not stack:
                leftlimit[i] = 0
            else:
                while stack and  heights[stack[-1]]>=heights[i]:
                    stack.pop()
                top = stack[-1]+1 if stack else 0
                leftlimit[i] = top
            stack.append(i)
        stack = []

        for i in range(len(heights)-1,-1,-1):
            if not stack:
                rightlimit[i] = len(heights)-1
            else:
                while stack and heights[stack[-1]]>=heights[i]:
                    stack.pop()
                top = stack[-1]-1 if stack else len(heights)-1
                rightlimit[i] = top
            stack.append(i)
        maxarea = 0
        for i in range(len(heights)):
            area = (rightlimit[i]-leftlimit[i]+1)*heights[i]
            maxarea = max(area,maxarea)
        return maxarea