# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if l1 is None or l2 is None:
            return None

        stack_left_nums = []
        stack_right_nums = []

        while l1 is not None or l2 is not None:
            if l1 is not None:
                stack_left_nums.append(str(l1.val))
                l1 = l1.next
            if l2 is not None:
                stack_right_nums.append(str(l2.val))
                l2 = l2.next

        head = None
        for node in str(int("".join(stack_left_nums[::-1])) + int("".join(stack_right_nums[::-1])))[::-1]:
            if head is None:
                head = ListNode(node)
                current = head
            else:
                current.next = ListNode(node)
                current = current.next
        return head


node1 = ListNode(1)
node2 = ListNode(8)
#node3 = ListNode(3)

node4 = ListNode(0)
#node5 = ListNode(6)
#node6 = ListNode(4)

node1.next = node2
#node2.next = node3

#node4.next = node5
#node5.next = node6

s = Solution()
print(s.addTwoNumbers(node1, node4))
