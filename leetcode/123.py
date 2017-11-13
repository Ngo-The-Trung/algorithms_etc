# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/
# 123. Best Time to Buy and Sell Stock III
# status=done

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        N = len(prices)

        if N == 0:
            return 0

        best_bw = [0] * N
        best = prices[-1]


        for i in range(N - 1, -1, -1):
            best = max(prices[i], best)
            if i != N - 1:
                best_bw[i] = max(best_bw[i + 1], best - prices[i])
            else:
                best_bw[i] = best - prices[i]

        best_fw = [0] * N
        best = prices[0]
        for i in range(N):
            best = min(prices[i], best)
            if i > 0:
                best_fw[i] = max(best_fw[i - 1], prices[i] - best)
            else:
                best_fw[i] = prices[i] - best

        best = 0
        for i in range(N):
            best = max(best, best_fw[i] + best_bw[i])

        return best


print Solution().maxProfit([1,2,3,2,1,2,3])
