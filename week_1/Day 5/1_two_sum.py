# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myHashMap = {}

        for i, val in enumerate(nums):
            diff = target - val

            if diff in myHashMap:
                return [myHashMap[diff], i]
            
            myHashMap[val] = i
        