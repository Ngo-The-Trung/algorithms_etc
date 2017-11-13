# https://leetcode.com/problems/product-of-array-except-self/description/
# 238. Product of Array Except Self
# status=done


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        if N == 0:
            return []

        result = [1] * N
        result[0] = nums[0]
        for i in range(1, N):
            result[i] = result[i - 1] * nums[i]

        right_prod = 1
        for i in range(N - 1, -1, -1):
            if i == 0:
                left_prod = 1
            else:
                left_prod = result[i - 1]
            result[i] = left_prod * right_prod
            right_prod *= nums[i]

        return result


print Solution().productExceptSelf([1,2,3,4])
