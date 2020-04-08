# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def display_linkedlist(head):
    current = head
    while current is not None:
        print(current.val, "->", end="")
        current = current.next

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None:
            return None

        if head.next is None:
            return head

        current = head
        stack = []
        stack.append(current)

        while current is not None:
            next_node = current.next
            current.next = None
            stack.append(current)
            current = next_node

        index = 0
        while len(stack) > 0:
            if index == 0:
                head = stack.pop()
                current = head
                index = index + 1
            else:
                if len(stack) != 1:
                    current.next = stack.pop()
                    current = current.next
                else:
                    current.next = None
                    stack.pop()
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
print(display_linkedlist(s.reverseList(node1)))
