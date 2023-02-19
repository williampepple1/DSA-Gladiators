"""
Given an array of meeting time intervals where intervals[i] = [starti, endi],
 return the minimum number of conference rooms required.

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Link: https://leetcode.com/problems/meeting-rooms-ii/

N.B: Fom the input, go ahead to define your method and argument(s) you suggest it should take.


"""


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """

    def minMeetingRooms(self, intervals):
        start = sorted([i.start for i in intervals])
        end = sorted([i.start for i in intervals])

        result, count = 0, 0
        s, e = 0, 0
        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1

            else:
                e += 1
                count -= 1

            result = max(result, count)

        return result
