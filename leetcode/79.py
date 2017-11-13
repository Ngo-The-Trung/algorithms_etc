# https://leetcode.com/problems/word-search/description/
# 79. Word Search

# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
# status=done

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(word) == 0:
            return False

        stack = []
        directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]

        n_rows = len(board)
        n_cols = len(board[0])

        def dfs(board, r, c, index):
            if board[r][c] != word[index]:
                return False

            if index == len(word) - 1:
                return True

            for dx, dy in directions:
                nx, ny = r + dx, c + dy
                if not (0 <= nx < n_rows and 0 <= ny < n_cols):
                    continue
                tmp = board[r][c]
                board[r][c] = None
                if dfs(board, nx, ny, index + 1):
                    board[r][c] = tmp
                    return True
                board[r][c] = tmp

        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if dfs(board, i, j, 0):
                    return True

        return False


board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

solution = Solution()
print solution.exist(board, "ABCCED")
print solution.exist(board, "SEE")
print solution.exist(board, "ABCB")

board = [
  ['A'],
]
print solution.exist(board, "A")
