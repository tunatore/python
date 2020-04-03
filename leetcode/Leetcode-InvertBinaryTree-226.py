from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if root is None:
            return None

        q = deque()
        q.append(root)
        return self.create_tree(q)

    def create_tree_recursive(self, root):
        if root is None:
            return None

        node = TreeNode(root.val)
        node.left = self.create_tree_recursive(root.right)
        node.right = self.create_tree_recursive(root.left)
        return node

    def create_tree(self, q):
        root = None
        while not len(q) == 0:
            node = q.popleft()
            if root is None:
                root = node
            if node is None:
                continue
            if node:
                node.left, node.right = node.right, node.left
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            print(node.val, end="->")
        return root


t1 = TreeNode(4)
t1.left = TreeNode(2)
t1.right = TreeNode(7)
t1.left.left = TreeNode(1)
t1.left.right = TreeNode(3)
t1.right.left = TreeNode(6)
t1.right.right = TreeNode(9)

s = Solution()
s.invertTree(t1)



