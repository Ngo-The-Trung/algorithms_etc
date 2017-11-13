# https://leetcode.com/problems/trapping-rain-water/description/
# 42. Trapping Rain Water
# status=done


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        N = len(height)
        if N == 0:
            return 0

        left_bar = [0] * N
        right_bar = [0] * N

        left_bar[0] = height[0]
        right_bar[-1] = height[-1]

        for i in range(1, N):
            left_bar[i] = max(left_bar[i - 1], height[i])

        for i in range(N - 2, -1, -1):
            right_bar[i] = max(right_bar[i + 1], height[i])

        total = 0
        for i, h in enumerate(height):
            total += min(left_bar[i], right_bar[i]) - h

        return total


print Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])
print Solution().trap([4,1,0,2,1,0,1,3,2,1,2,4])
