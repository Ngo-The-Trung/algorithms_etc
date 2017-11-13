class Solution:
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        N = len(num)
        if N == 0 or N <= k:
            return "0"

        zero = [0] * N
        zero[-1] = -1
        last_zero = -1 if num[N - 1] != '0' else N - 1
        for i in range(N - 2, -1, -1):
            zero[i] = last_zero
            if num[i] == '0':
                last_zero = i
        K = k
        i = 0
        while i < N and k > 0:
            if zero[i] == -1:
                break
            else:
                steps = zero[i] - i
                if steps <= k:
                    k -= steps
                    i = zero[i]
                else:
                    break
        print i, k


from helper import ObjectProxy
s = ObjectProxy(Solution())
s.removeKdigits("1432219", 3)
s.removeKdigits("10200", 1)
s.removeKdigits("10", 2)
