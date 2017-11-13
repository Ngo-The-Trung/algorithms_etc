# status=not_done

class Solution(object):
    def mergeAndCount(self, nums, counter):
        N = len(nums)

        if N == 1:
            return 0, nums

        mid = N / 2
        left_count, left_sorted = self.mergeAndCount(nums[0:mid])
        right_count, right_sorted = self.mergeAndCount(nums[mid:N])
        count = left_count + right_count

        for i in range(mid):
            right = 0
            while right < N - mid and right_sorted[right] * 2 < left_sorted[i]:
                right += 1
            count += right

        left = 0
        right = 0

        for i in range(N):
            if left == len(left_sorted):
                nums[i] = right_sorted[right]
                right += 1
            elif right == len(right_sorted):
                nums[i] = left_sorted[left]
                left += 1
            else:
                if left_sorted[left] < right_sorted[right]:
                    nums[i] = left_sorted[left]
                    left += 1
                else:
                    nums[i] = right_sorted[right]
                    right += 1
        return count, nums


    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count, _ = self.mergeAndCount(nums, [0] * len(nums))
        return count

# print Solution().reversePairs([1,3,2,3,1])
# print Solution().reversePairs([2,4,3,5,1])

import random
worst = [random.randint(0, 10**5) for i in range(5000)]
print Solution().reversePairs(worst)
