# Construct Binary Tree from Preorder and Inorder Traversal

class Frame(object):

    def __init__(self, inorder_left, inorder_right, IP=0):
        self.IP = IP
        self.inorder_left = inorder_left  # inclusive
        self.inorder_right = inorder_right  # exclusive

        self.mid_p = 0

        self.node = None

    def __str__(self):
        return "IP = {}, left = {}, right = {}".format(self.IP, self.inorder_left, self.inorder_right)


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        start, wait_left, wait_right, returning = 0, 1, 2, 3
        stack_result = None

        stack = [ None ] * (len(preorder) + 10)
        stack_i = 0
        stack[0] = Frame(0, len(preorder))

        while stack_i >= 0:
            frame = stack[stack_i]

            if frame.IP == start:
                if frame.inorder_left == frame.inorder_right:
                    frame.IP = returning
                    stack_result = None
                    continue

                s = set()
                for i in range(frame.inorder_left, frame.inorder_right):
                    s.add(inorder[i])

                for v in preorder:
                    if v in s:
                        mid = v
                        break

                node = TreeNode(mid)
                frame.node = node

                for i in range(frame.inorder_left, frame.inorder_right):
                    v = inorder[i]
                    if v == mid:
                        frame.mid_p = i

                frame.inorder = frame.preorder = None

                frame.IP = wait_left
                stack_i += 1
                stack[stack_i] = Frame(frame.inorder_left, frame.mid_p)

            elif frame.IP == wait_left:
                # evalutes right
                frame.node.left = stack_result
                frame.IP = wait_right

                stack_i += 1
                stack[stack_i] = Frame(frame.mid_p + 1, frame.inorder_right)

            elif frame.IP == wait_right:
                frame.node.right = stack_result
                stack_result = frame.node
                frame.IP = returning

            else:
                stack[stack_i] = None
                stack_i -= 1

        return stack_result
