# https://leetcode.com/problems/meeting-rooms-ii/description/
# 253. Meeting Rooms II
# status=done
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
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
        last = -1
        min_rooms = 0
        # print bounds
        for i, (v, bound_type) in enumerate(bounds):
            if bound_type == start:
                last = v
                if count == 0:
                    if left != -1:
                        result.append(Interval(left, right))
                    left = v
                count += 1
            else:
                if count > min_rooms:
                    if last != -1 and last == v:
                        min_rooms = count -1
                        last = -1
                    else:
                        min_rooms = count
                right = v
                count -= 1
        if left != -1:
            result.append(Interval(left, right))
        return min_rooms

print Solution().minMeetingRooms([Interval(0, 30),Interval(5, 10),Interval(15, 20)])
print Solution().minMeetingRooms([Interval(13, 15),Interval(1, 13)])
