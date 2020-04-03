# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        d = dict([])

        if head is None or head.next is None:
            return False

        current = head
        while current is not None:
            if current.next is None:
                return False
            if current.next in d:
                return True
            else:
                d[current] = current
                current = current.next
        return False


node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)
node5 = ListNode(5)
node6 = ListNode(-4)
node7 = ListNode(7)
node8 = ListNode(8)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8

s = Solution()
print(s.hasCycle(node1))
