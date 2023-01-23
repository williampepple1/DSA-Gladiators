# Given an integer array nums, return true if any value appears at least twice in the array,
#  and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
		checker = {}
		for num in nums:
			if checker[num] is True:
				return True
			else:
				checker[num] = True
		return False


		"""
		Alternate Solution
		return True if len(nums) != len(set(nums)) else False
		"""
