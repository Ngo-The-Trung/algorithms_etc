# https://leetcode.com/problems/merge-intervals/description/
# 56. Merge Intervals
# Given a collection of intervals, merge all overlapping intervals.
# status=done

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return "(%s, %s)" % (self.start, self.end)

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        start = 0
        end = 1

        bounds = []
        for i in intervals:
            bounds.append((i.start, start))
            bounds.append((i.end, end))
        bounds.sort()

        result = []
        left = right = -1
        count = 0
        # print bounds
        for i, (v, bound_type) in enumerate(bounds):
            if bound_type == start:
                if count == 0:
                    if left != -1:
                        result.append(Interval(left, right))
                    left = v
                count += 1
            else:
                right = v
                count -= 1
        if left != -1:
            result.append(Interval(left, right))
        return result

solution = Solution()
print solution.merge([
    Interval(1, 3),
    Interval(2, 6),
    Interval(8, 10),
    Interval(15,18)
])
print solution.merge([
    Interval(1, 4),
    Interval(0, 2),
    Interval(3, 5)
])
