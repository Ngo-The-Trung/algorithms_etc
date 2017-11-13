# https://leetcode.com/problems/minimum-window-substring/description/
# 76. Minimum Window Substring
# status=done
import collections


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        counter = {key:0 for key in t}
        expected = collections.Counter(t)

        N = len(s)

        if N == 0:
            return ""

        seen = 0
        left = right = 0
        complete = False

        for right, c in enumerate(s):
            if c not in counter:
                continue

            if counter[c] < expected[c]:
                seen += 1
            counter[c] += 1

            if seen == len(t):
                complete = True
                break

        if not complete:
            # print counter, seen
            return ""

        while left < N:
            if s[left] in counter:
                if counter[s[left]] == expected[s[left]]:
                    break
                counter[s[left]] -= 1
            left += 1

        best_left = left
        best_right = right

        while True:
            right += 1

            while right < N and s[right] not in counter:
                right += 1

            if right == N:
                break

            counter[s[right]] += 1

            while left < N:
                if s[left] in counter:
                    if counter[s[left]] == expected[s[left]]:
                        break
                    counter[s[left]] -= 1
                left += 1

            if best_right - best_left > right - left:
                best_right = right
                best_left = left

        return s[best_left:best_right + 1]

print Solution().minWindow("A", "A")
print Solution().minWindow("A", "AA")
print Solution().minWindow("A", "AB")
print Solution().minWindow("AB", "A")
print Solution().minWindow("AA", "AA")
print Solution().minWindow("ADOBECODEBANC", "ABC")
print Solution().minWindow("bdab", "ab")
