# Pow(x, n)

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1

        if n < 0:
            n = -n
            neg = True
        else:
            neg = False

        modulo = []
        while n > 1:
            m = n % 2
            modulo.append(m)
            if m == 1:
                n -= 1
            else:
                n /= 2

        prod = x
        for i in modulo[::-1]:
            if i == 0:
                prod *= prod
            else:
                prod *= x

        return prod if not neg else 1.0/prod
