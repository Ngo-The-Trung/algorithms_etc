# https://leetcode.com/problems/sliding-window-median/description/
# 480. Sliding Window Median
# status=not_done

from heapq import heappush as push, heappop as pop, heapify

class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        first_window = sorted(nums[:k])
        median = k / 2
        left_heap = first_window[:median + 1]
        if k % 2 == 1:
            right_heap = first_window[median:]
        else:
            right_heap = first_window[median + 1:]

        heapify(left_heap)
        heapify(right_heap)
