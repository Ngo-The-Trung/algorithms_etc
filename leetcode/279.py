# https://leetcode.com/problems/perfect-squares/description/
# 279. Perfect Squares
# status=not_done

import math


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = 0
        while n > 0:
            sqrt = int(math.sqrt(n))
            total += 1
            n -= sqrt ** 2
        return total


print Solution().numSquares(12)
