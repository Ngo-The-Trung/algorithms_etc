# Populating Next Right Pointers in Each Node

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root != None:
            self._connect(root.left, root.right)

    def _connect(self, left, right):
        if left != None:
            self._connect(left.left, left.right)
            left.next = right
        if right != None:
            self._connect(right.left, right.right)

        if left != None and right != None:
            self._connect(left.right, right.left)
