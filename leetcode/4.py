# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
# 4. Median of Two Sorted Arrays
# status=not_done
from bisect import bisect_left as bs


class Solution(object):
    def findMedian(self, nums):
        L = len(nums)
        median = L / 2
        if L % 2 == 0:
            return (nums[median] + nums[median + 1]) / 2

        return nums[median]

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums2) == 0:
            return self.findMedian(nums1)

        if len(nums1) == 0:
            return self.findMedian(nums2)

        total_len = len(nums1) + len(nums2)
        median_index = total_len / 2

        left = 0
        right = len(nums1)

        while True:
            mid_1 = (left + right) / 2

            if mid_1 >= len(nums1):
                break

            mid_2 = bs(nums2, nums1[mid_1])

            lesser_count = mid_1 + mid_2
            if lesser_count == median_index or lesser_count == median_index + 1:
                break

            if lesser_count > median_index:
                right = mid_1
            else:
                left = mid_1 + 1

        return mid_1, mid_2


solve = Solution().findMedianSortedArrays

print solve([1,2,3,4], [5,6,7])
print solve([1,3,5,7], [2,4,6])
print solve([1], [2,3,4,5,6,7])
print solve([1,2,3,4,5,6], [7])
print solve([], [1,2,3,4,5,6,7])
print solve([1,2,3,4,5,6,7], [])
