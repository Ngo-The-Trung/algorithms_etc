# https://leetcode.com/problems/missing-number/description/
# 268. Missing Number
# status=done

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = 0
        m = len(nums)
        _max = 0
        for n in nums:
            s += n
            _max = max(_max, n)
        if _max < m:
            return m
        return (m * (m + 1) / 2) - s
