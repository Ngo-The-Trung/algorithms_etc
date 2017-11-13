# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
# 297. Serialize and Deserialize Binary Tree
# Definition for a binary tree node.
# status=done

# Pre order traversal and queue for both serde

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        nums = []
        q = [root]

        while len(q) > 0:
            top = q[0]
            q = q[1:]
            if not top:
                nums.append(None)
            else:
                nums.append(top.val)
                q = [top.left, top.right] + q
        return "\n".join(map(lambda x: "n" if x is None else str(x), nums))


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        lines = data.splitlines()
        left = 0
        right = 1

        if lines[0] == "n":
            return None

        root = TreeNode(int(lines[0]))

        q = [(root, left), (root, right)]
        i = 1
        while len(q) > 0:
            node, branch = top = q[0]
            q = q[1:]

            child = None if lines[i] == "n" else TreeNode(int(lines[i]))
            if branch == left:
                node.left = child
            else:
                node.right = child

            if child:
                q = [(child, left), (child, right)] + q

            i += 1

        return root



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(6)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(8)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

codec = Codec()
ser = codec.serialize(root)
root = codec.deserialize(ser)
print ser == codec.serialize(root)
