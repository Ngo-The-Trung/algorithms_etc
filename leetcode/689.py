# https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/description/
# 689. Maximum Sum of 3 Non-Overlapping Subarrays
# In a given array nums of positive integers, find three non-overlapping subarrays with maximum sum.
#
# Each subarray will be of size k, and we want to maximize the sum of all 3*k entries.
#
# Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.
# status=done

class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        N = len(nums)
        k_sums_len = N - k + 1
        k_sums = [0] * k_sums_len

        total = 0
        for i in range(k):
            total += nums[i]
        k_sums[0] = total

        for i in range(k, N):
            total = total + nums[i] - nums[i - k]
            k_sums[i - k + 1] = total

        # print k_sums
        best = [None] * (N + 1)
        prev = [None] * (N + 1)
        for i in range(k):
            best[i] = [0, -1, -1, -1]
            prev[i] = [-1, -1, -1, -1]
        for i in range(k, N + 1):
            best[i] = [-1, -1, -1, -1]
            prev[i] = [-1, -1, -1, -1]
            current_k_sum = k_sums[i - k]
            # print best
            for j in range(1, 4):
                # print i, j, k, best[i - k][j - 1]
                if best[i - k][j - 1] == -1:
                    s1 = current_k_sum
                else:
                    s1 = best[i - k][j - 1] + current_k_sum

                if best[i - 1][j] == -1:
                    s2 = -1
                else:
                    s2 = best[i - 1][j]

                if s1 > s2:
                    best[i][j] = s1
                    prev[i][j] = (i - k, j - 1)
                else:
                    best[i][j] = s2
                    prev[i][j] = prev[i - 1][j]
        result = []
        cur = prev[-1][3]

        while cur != -1:
            i, j = cur
            result.append(i)
            cur = prev[i][j]

        # print(best)

        return list(reversed(result))


print Solution().maxSumOfThreeSubarrays([1,2,1,2,6,7,5,1], 2)
# print Solution().maxSumOfThreeSubarrays([1,2], 2)
print Solution().maxSumOfThreeSubarrays([4,5,10,6,11,17,4,11,1,3], 1)
