# https://leetcode.com/problems/decode-ways/description/
# 91. Decode Ways
# status=done

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        if N == 0:
            return 0
        if s[0] == '0':
            return 0
        count = [0] * N
        count[0] = 1

        for i in range(1, N):
            v = int(s[i - 1] + s[i])
            if 10 <= v <= 26:
                if i > 1:
                    count[i] += count[i - 2]
                else:
                    count[i] += 1
            if s[i] != '0':
                count[i] += count[i - 1]

        return count[-1]


s = Solution()
