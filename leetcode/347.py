# https://leetcode.com/problems/top-k-frequent-elements/description/
# 347. Top K Frequent Elements
# status=done

import collections
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        fr = collections.Counter(nums).items()
        fr.sort(key=lambda t: -t[1])
        return map(lambda t: t[0], fr[:k])
