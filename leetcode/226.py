# Invert Binary Tree

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return
        tmp = root.left
        root.left = root.right
        root.right = tmp
        if type(root.left) == TreeNode:
            self.invertTree(root.left)
        if type(root.right) == TreeNode:
            self.invertTree(root.right)
        return root
