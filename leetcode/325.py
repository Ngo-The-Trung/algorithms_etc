
# https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/description/
# 325. Maximum Size Subarray Sum Equals k
# status=done

# Change all 0 to -1, then calculate the prefix sum array
# The problem becomes: Find 2 positions on the prefix sum array where the
# difference is 0
class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix = [0] * (len(nums) + 1)
        prefix[0] = 0
        for i in range(0, len(nums)):
            prefix[i + 1] = prefix[i] + nums[i]
        seen = {}
        for i, p in enumerate(prefix):
            seen[p] = i

        max_len = 0
        for i, p in enumerate(prefix):
            if (k + p) in seen and seen[k + p] > i:
                max_len = max(max_len, seen[k + p] - i)
        return max_len


s = Solution()
print s.maxSubArrayLen([1, -1, 5, -2, 3], 3)
print s.maxSubArrayLen([-2,-1,2,1], 1)
