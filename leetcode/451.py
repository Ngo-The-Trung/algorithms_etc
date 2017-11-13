# https://leetcode.com/problems/sort-characters-by-frequency/description/
# 451. Sort Characters By Frequency
# status=done
import collections
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        fr = collections.Counter(s).items()
        fr.sort(key=lambda t: -t[1])
        return ''.join([c * f for c, f in fr])
