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

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None:
            return None

        if head.next is None:
            return head

        current = head
        previous = None
        head = None
        while current is not None:
            if current.next is not None:
                temp = current.next
                current.next = temp.next
                temp.next = current
                if previous is not None:
                    previous.next = temp
                    previous = current
                if previous is None:
                    previous = current
                current = current.next
                if head is None:
                    head = temp
            else:
                current = current.next
        return head


node1 = ListNode(2)
node2 = ListNode(5)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(6)
node6 = ListNode(2)
node7 = ListNode(2)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

s = Solution()
print(display_linkedlist(s.swapPairs(node1)))