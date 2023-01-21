# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        l, r = 0, len(height) - 1
        leftmax, rightmax = height[l], height[r]
        res = 0
        
        while l < r:
            if leftmax < rightmax:
                l += 1
                leftmax = max(leftmax, height[l])
                res += leftmax - height[l]
                
            else:
                r -= 1
                rightmax = max(rightmax, height[r])
                res += rightmax - height[r]
                
        return res