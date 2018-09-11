# Author: Allen Anker
# Created by Allen Anker on 11/09/2018
"""
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
"""


class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution:
    def max_points(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        l = len(points)
        m = 0
        for i in range(l):
            dic = {str(i): 1}
            same = 0
            for j in range(i + 1, l):
                tx, ty = points[j].x, points[j].y
                if tx == points[i].x and ty == points[i].y:
                    same += 1
                    continue
                # for every i, dic['i'] increments every time a point with the same x value is found
                if points[i].x == tx:
                    slope = str(i)
                else:
                    # else the denominator can't be zero
                    if points[i].x == points[i].y == 0:
                        slope = (1 - ty) * 1.0 / (1 - tx) if tx is not 1 else (2 - ty) * 1.0 / (2 - tx)
                    else:
                        slope = (points[i].y - ty) * 1.0 / (points[i].x - tx)
                if slope not in dic:
                    dic[slope] = 1
                dic[slope] += 1
            m = max(m, max(dic.values()) + same)
        return m


points = [Point(0, 0), Point(94911151, 94911150), Point(94911152, 94911151)]
solution = Solution()
print(solution.max_points(points))
print(94911151 / 94911152 * 1.0 == 94911152 / 94911153 * 1.0)
