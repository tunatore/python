# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def display_linkedlist(head):
    current = head
    while current is not None:
        print(current.val, end="->")
        current = current.next


from collections import deque


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if k < 0:
            return None

        if k == 0:
            return head

        list = []
        current = head
        while current is not None:
            list.append(current.val)
            current = current.next

        circular_queue = deque(list)
        circular_queue.rotate(k)

        head = None
        for node in circular_queue:
            if head is None:
                head = ListNode(node)
                current = head
            else:
                current.next = ListNode(node)
                current = current.next
        return head


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

s = Solution()
print(display_linkedlist(s.rotateRight(node1, 4)))
