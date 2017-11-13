# https://leetcode.com/problems/maximum-swap/description/
# 670. Maximum Swap
# status=done

class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        orig = num
        digits = []
        while num > 0:
            d = num % 10
            num = num / 10
            digits.append(d)
        N = len(digits)
        max_digit = [0] * N
        for i in range(N):
            if i == 0:
                max_digit[i] = 0
            else:
                if digits[max_digit[i - 1]] >= digits[i]:
                    max_digit[i] = max_digit[i - 1]
                else:
                    max_digit[i] = i
        found = False
        for i in range(N - 1, -1, -1):
            if digits[max_digit[i]] > digits[i]:
                digits[max_digit[i]], digits[i] = digits[i], digits[max_digit[i]]
                found = True
                break

        if not found:
            return orig

        v = 0
        for i in range(N - 1, -1, -1):
            v = v * 10 + digits[i]
        return v

print Solution().maximumSwap(2736)
print Solution().maximumSwap(9973)
print Solution().maximumSwap(1993)
