# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def display_linkedlist(head):
    current = head
    while current is not None:
        print(current.val)
        current = current.next


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return None

        if head.next is None and head.val != val:
            return head

        current = head
        previous = head
        while current is not None:
            if current.val == val:
                if head.val == val:
                    head = current.next
                    current.next = None
                    current = head
                    previous = head
                else:
                    previous.next = current.next
                    next_node = current.next
                    if current is not None:
                        current.next = None
                    current = next_node
            else:
                previous = current
                current = current.next
        return head


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(6)
node4 = ListNode(3)
node5 = ListNode(4)
node6 = ListNode(5)
node7 = ListNode(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

s = Solution()
print(display_linkedlist(s.removeElements(node1, 6)))
