# Given an integer array nums, return true if any value appears at least twice in the array,
#  and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_set = set()

        for i in nums:
            if i in my_set:
                return True
            my_set.add(i)
        return False


# Time complexity (O)n
