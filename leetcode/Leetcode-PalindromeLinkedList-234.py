# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if head is None:
            return True

        if head.next is None:
            return head

        linked_list_stack = []
        while head is not None:
            linked_list_stack.append(head.val)
            head = head.next
        return linked_list_stack == list(reversed(linked_list_stack))


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(3)
node5 = ListNode(2)
node6 = ListNode(1)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

s = Solution()
print(s.isPalindrome(node1))
