# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.


class Solution:
    def trap(self, height: List[int]) -> int:

        left, right = 0, len(height) - 1
        maxLeft, maxRight = height[left], height[right]
        trapped_water = 0

        while left < right:
            if height[left] <= height[right]:
                trapped_water += max(0, maxLeft - height[left])
                left += 1
                maxLeft = max(maxLeft, height[left])

            else:
                trapped_water += max(0, maxRight - height[right])
                right -= 1
                maxRight = max(maxRight, height[right])

        return trapped_water
