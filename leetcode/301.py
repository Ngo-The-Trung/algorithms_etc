# https://leetcode.com/problems/remove-invalid-parentheses/description/
# Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.
# status=not_done

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        invalid = 0
        stack = 0
        for c in s:
            if c == '(':
                stack += 1
            elif c == ')':
                if stack == 0:
                    invalid += 1
                else:
                    stack -= 1
        invalid += stack

        return invalid
 -> ["()()()", "(())()"]
 -> ["(a)()()", "(a())()"]
")(" -> [""]
print Solution().removeInvalidParentheses("()())()")
"(a)())()"
