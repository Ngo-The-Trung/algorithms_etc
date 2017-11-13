# https://leetcode.com/problems/house-robber/description/
# 198. House Robber
# status=done

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        if N == 0:
            return 0

        best1 = best2 = 0
        best0 = nums[0]

        for i in range(1, N):
            best2, best1 = best1, best0
            best0 = max(nums[i] + best2, best1)

        return best0

from helper import ObjectProxy
s = ObjectProxy(Solution())
s.rob([1])
s.rob([1, 2])
s.rob([1, 2, 3, 4])
s.rob([2, 7, 9, 3, 1])
