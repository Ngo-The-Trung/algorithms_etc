# Missing Number

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = 0
        s = 0
        zeroed = False
        for i in nums:
            if i == 0:
                zeroed = True
            if i > m:
                m = i
            s += i
        t = (m + 1) * m / 2
        if s == t:
            if zeroed:
                return m + 1
            else:
                return 0
        return t - s
