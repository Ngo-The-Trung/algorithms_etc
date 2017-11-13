# https://leetcode.com/problems/contiguous-array/description/
# 525. Contiguous Array
# status=done

# Change all 0 to -1, then calculate the prefix sum array
# The problem becomes: Find 2 positions on the prefix sum array where the
# difference is 0

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix = [0] * (len(nums) + 1)
        prefix[0] = 0
        for i in range(0, len(nums)):
            prefix[i + 1] = prefix[i] + (1 if nums[i] == 1 else -1)
        seen = {}
        for i, p in enumerate(prefix):
            seen[p] = i
        max_len = 0
        for i, p in enumerate(prefix):
            if seen[p] > i:
                max_len = max(max_len, seen[p] - i)
        return max_len


s = Solution()
print s.findMaxLength([0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1])
print s.findMaxLength([1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0])
print s.findMaxLength([0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1])
