from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


# Time complexity O(N) and Space complexity O(N)
def traverse(root):
    result = []

    if root is None:
        return result

    q = deque()
    q.append(root)

    while not len(q) == 0:
        current_level = []
        for _ in range(len(q)):
            node = q.popleft()
            current_level.append(node.val)
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        result.append(current_level)
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(traverse(root)))


main()
