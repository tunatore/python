from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


# Time complexity O(N) and Space complexity O(N)
def find_minimum_depth(root):

    if root is None:
        return 0

    q = deque()
    q.append(root)
    level_num = 0

    while not len(q) == 0:
        level_num += 1
        for _ in range(len(q)):
            node = q.popleft()
            if node.left is None and node.right is None:
                return level_num
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
    return level_num


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


main()
