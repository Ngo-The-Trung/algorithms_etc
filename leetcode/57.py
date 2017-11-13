# https://leetcode.com/problems/insert-interval/description/
# 57. Insert Interval

# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

# You may assume that the intervals were initially sorted according to their start times.
# status=done

class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return "(%s, %s)" % (self.start, self.end)

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        intervals.append(newInterval)

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
print solution.insert([
    Interval(1,2),
    Interval(3,5),
    Interval(6,7),
    Interval(8,10),
    Interval(12,16)
], Interval(4, 9))
