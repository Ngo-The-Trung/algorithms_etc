# https://leetcode.com/problems/maximum-length-of-pair-chain/description/
# 646. Maximum Length of Pair Chain
# status=not_done

class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        edge = []
        for (left, right) in pairs:
            edge.append((left, 0))
            edge.append((right, 1))

        edge.sort()

        count = 0
        opening = False
        for (edge, edge_type) in edge:
            if not opening and edge_type == 1:
                count += 1

