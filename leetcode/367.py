class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        x = self.mySqrt(num)
        return x * x == num

    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 0
        right = x

        while left + 1 < right:
            mid = (left + right) / 2
            _x = mid * mid
            if _x > x:
                right = mid
            elif _x < x:
                left = mid
            else:
                return mid

        if right * right <= x:
            return right
        return left
