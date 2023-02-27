# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array
# such that nums[i] == nums[j] and abs(i - j) <= k.
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        store2 = {}
        for i in range(len(nums)):

            if nums[i] in store2:
                if i - store2[nums[i]] <= k:
                    return True
                else:
                    store2[nums[i]] = i
            else:
                store2[nums[i]] = i

        return False
