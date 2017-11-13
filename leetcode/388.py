# https://leetcode.com/problems/longest-absolute-file-path/description/
# 388. Longest Absolute File Path

# status=done


class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        path_len = []
        level = 0
        cur_len = 0
        best = 0
        is_file = False

        for i, c in enumerate(input):
            if c == '\n' or i == len(input) - 1:
                if is_file:
                    if i == len(input) - 1:
                        cur_len += 1
                    if cur_len > best:
                        best = cur_len
                if level >= len(path_len):
                    path_len.append(cur_len)
                else:
                    path_len[level] = cur_len
                is_file = False
                level = 0
                cur_len = 0
            elif c == '\t':
                cur_len = path_len[level] + 1
                level += 1
            else:
                if c == '.':
                    is_file = True
                cur_len += 1

        return best

solution = Solution()
print solution.lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")
print solution.lengthLongestPath("a")
