# https://leetcode.com/problems/sparse-matrix-multiplication/description/
# 311. Sparse Matrix Multiplication
# status=not_done

class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        def mul(row, col):
            row, row_keys = row
            col, col_keys = col
            indices = row_keys.intersection(col_keys)
            # print indices
            return sum([row[i] * col[i] for i in indices])
        Arows = []
        Bcols = []
        for row in range(len(A)):
            d = {}
            Arows.append(d)
            for col in range(len(A[0])):
                if A[row][col] != 0:
                    d[col] = A[row][col]
        for row in range(len(A)):
            Arows[row] = (Arows[row], set(Arows[row].keys()))

        for col in range(len(B[0])):
            d = {}
            Bcols.append(d)
            for row in range(len(B)):
                if B[row][col] != 0:
                    d[row] = B[row][col]
        for col in range(len(Bcols)):
            Bcols[col] = (Bcols[col], set(Bcols[col].keys()))

        result = []
        # print Arows, Bcols
        for i in range(len(A)):
            row = []
            result.append(row)
            for j in range(len(B[0])):
                row.append(mul(Arows[i], Bcols[j]))
        return result


A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

# print Solution().multiply(A, B)

A = [
  [1, -5],
]

B = [
    [12], [-1]
]
print Solution().multiply(A, B)

A = [[0] * 100 for i in range(100)]
B = [[0] * 100 for i in range(100)]
print Solution().multiply(A, B)
