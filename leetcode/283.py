# https://leetcode.com/problems/move-zeroes/description/
# 283. Move Zeroes

# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
# status=done

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        if N == 0:
            return

        non_zero = zero = 0
        while True:
            while zero < N and nums[zero] != 0:
                zero += 1

            while non_zero < N and (nums[non_zero] == 0 or non_zero < zero):
                non_zero += 1

            if zero == N or non_zero == N:
                return

            if zero < non_zero:
                nums[zero], nums[non_zero] = nums[non_zero], nums[zero]


solution = Solution()
# nums = [0, 1, 0, 3, 12]
# solution.moveZeroes(nums)
# print nums
#
# nums = [0]
# solution.moveZeroes(nums)
# print nums
#
# nums = [1]
# solution.moveZeroes(nums)
# print nums
#
# nums = [1, 0]
# solution.moveZeroes(nums)
# print nums

nums = [1, 0, 1]
solution.moveZeroes(nums)
print nums
