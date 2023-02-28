"""
(This problem is an interactive problem.)

Each ship is located at an integer point on the sea represented by a cartesian plane, and each integer point may contain at most 1 ship.

You have a function Sea.hasShips(topRight, bottomLeft) which takes two points as arguments and returns true If there is at least one ship in the rectangle represented by the two points, including on the boundary.

Given two points: the top right and bottom left corners of a rectangle, return the number of ships present in that rectangle. It is guaranteed that there are at most 10 ships in that rectangle.

Submissions making more than 400 calls to hasShips will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.

Link: https://leetcode.com/problems/number-of-ships-in-a-rectangle/

N.B: Fom the input, go ahead to define your method and argument(s) you suggest it should take.

"""


# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
# class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        if bottomLeft.x > topRight.x or bottomLeft.y > topRight.y:
            return 0
        elif bottomLeft.x == topRight.x and bottomLeft.y == topRight.y:
            return int(sea.hasShips(topRight, bottomLeft))
        if not sea.hasShips(topRight, bottomLeft):
            return 0
        midx = (topRight.x + bottomLeft.x) // 2
        midy = (topRight.y + bottomLeft.y) // 2
        mid = Point(midx, midy)
        topLeftQ = self.countShips(sea, Point(mid.x, topRight.y), Point(bottomLeft.x, mid.y + 1))
        bottomLeftQ = self.countShips(sea, Point(mid.x, mid.y), bottomLeft)
        topRightQ = self.countShips(sea, topRight, Point(mid.x + 1, mid.y + 1))
        bottomRightQ = self.countShips(sea, Point(topRight.x, mid.y), Point(mid.x + 1, bottomLeft.y))
        return topLeftQ + bottomLeftQ + topRightQ + bottomRightQ
