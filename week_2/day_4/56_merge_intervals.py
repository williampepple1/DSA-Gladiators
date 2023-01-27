# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an
# array of the non-overlapping intervals that cover all the intervals in the input.
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sortedInterval = sorted(intervals, key=lambda x: x[0])

        currentInterval = sortedInterval[0]

        mergedInterval = [currentInterval]

        for nextInterval in sortedInterval:
            if currentInterval[1] >= nextInterval[0]:
                currentInterval[1] = max(currentInterval[1], nextInterval[1])

            else:
                mergedInterval.append(nextInterval)
                currentInterval = nextInterval

        return mergedInterval


        