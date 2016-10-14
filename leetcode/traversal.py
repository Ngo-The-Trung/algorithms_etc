class TreeNode(object):

    def __init__(self, x):
        self.val = x

    def __str__(self):
        return "<{}, {}, {}>".format(self.val, self.left, self.right)

    def pre_order(self):
        r = [self.val]
        r += self.left.pre_order() if self.left is not None else []
        r += self.right.pre_order() if self.right is not None else []
        return r

    def in_order(self):
        r = self.left.in_order() if self.left is not None else []
        r += [self.val]
        r += self.right.in_order() if self.right is not None else []
        return r

    def post_order(self):
        r = self.left.post_order() if self.left is not None else []
        r += self.right.post_order() if self.right is not None else []
        r += [self.val]
        return r
