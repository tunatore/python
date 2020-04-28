# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        remaining_nodes = []
        if root.val not in to_delete:
            remaining_nodes.append(root)

        self.remove(root, to_delete, remaining_nodes)
        return remaining_nodes

    def display_tree(self, remaining_nodes):
        for node in remaining_nodes:
            self.print_tree(node)

    def print_tree(self, node):
        print(node.val, end="->")
        if node.left is not None:
            self.print_tree(node.left)
        if node.right is not None:
            self.print_tree(node.left)

    def remove(self, root, to_delete, remaining_nodes):

        if root is None:
            return None

        root.left = self.remove(root.left, to_delete, remaining_nodes)
        root.right = self.remove(root.right, to_delete, remaining_nodes)

        if root.val in to_delete:
            if root.left is not None:
                remaining_nodes.append(root.left)
            if root.right is not None:
                remaining_nodes.append(root.right)
            return None
        return root


t = TreeNode(1)
t.left = TreeNode(2)
t.left.left = TreeNode(4)
t.left.right = TreeNode(5)
t.right = TreeNode(3)
t.right.left = TreeNode(6)
t.right.right = TreeNode(7)

s = Solution()
s.display_tree(s.delNodes(t, [3, 5]))  # [[1,2,null,4],[6],[7]]
