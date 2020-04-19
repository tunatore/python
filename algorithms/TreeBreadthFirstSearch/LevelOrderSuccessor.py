# tree breadth first search
from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


# Time complexity O(N) and space complexity O(N)
def find_successor(root, key):
    if root is None:
        return None

    q = deque()
    q.append(root)

    while not len(q) == 0:  # while queue is not empty
        nodes_count = len(q)
        while nodes_count != 0:  # for each node in the level
            node = q.popleft()
            if node.val == key and node.left is None:
                return q.popleft()
            if node.left is not None:
                if node.val == key:
                    return node.left
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
            nodes_count -= 1
    return None


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    result = find_successor(root, 12)
    if result:
        print(result.val)
    result = find_successor(root, 9)
    if result:
        print(result.val)


main()
