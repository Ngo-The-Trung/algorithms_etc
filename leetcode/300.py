# https://leetcode.com/problems/longest-increasing-subsequence/description/
# 300. Longest Increasing Subsequence
# status=done
import bisect


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        if N == 0:
            return 0

        best = [0] * N
        len_best = 0

        for i, v in enumerate(nums):
            if i == 0:
                best[0] = v
                len_best += 1
            else:
                p = bisect.bisect_left(best, v, 0, len_best)
                if p == len_best:
                    best[len_best] = v
                    len_best += 1
                elif best[p] > v:
                    best[p] = v
        return len_best

print Solution().lengthOfLIS([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])
