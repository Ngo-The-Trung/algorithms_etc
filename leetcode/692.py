# https://leetcode.com/problems/top-k-frequent-words/description/
# 692. Top K Frequent Words
# status=done
import collections
class Solution(object):
    def topKFrequent(self, words, k):
        fr = collections.Counter(words).items()
        fr.sort(key=lambda t: (-t[1], t[0]))
        return map(lambda t: t[0], fr[:k])
