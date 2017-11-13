# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
# 17. Letter Combinations of a Phone Number
# status=done
import itertools

phone = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == '':
            return []

        return [''.join(prod) for prod in itertools.product(*[phone[d] for d in digits])]

print Solution().letterCombinations('23')
