# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
# 215. Kth Largest Element in an Array
# status=done
from heapq import heappush as push, heappop as pop

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []

        for n in nums:
            if len(heap) < k:
                push(heap, n)
            else:
                if heap[0] < n:
                    pop(heap)
                    push(heap, n)

        return heap[0]

print Solution().findKthLargest([3,2,1,5,6,4], 1)
print Solution().findKthLargest([3,2,1,5,6,4], 2)
print Solution().findKthLargest([3,2,1,5,6,4], 3)
print Solution().findKthLargest([3,2,1,5,6,4], 4)
print Solution().findKthLargest([3,2,1,5,6,4], 5)
print Solution().findKthLargest([3,2,1,5,6,4], 6)
