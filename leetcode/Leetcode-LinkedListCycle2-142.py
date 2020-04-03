# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None or head.next is None:
            return None

        slow = head
        fast = head
        cycle_length = 0
        while fast is not None:
            slow = slow.next
            if fast.next is not None:
                fast = fast.next.next
            else:
                fast = None
            if slow == fast:
                cycle_length = self.calculate_cycle_length(slow)
                break

        if cycle_length == 0:
            return None

        return self.find_start_cycle(head, cycle_length)

    def calculate_cycle_length(self, slow):
        current = slow
        cycle_length = 0
        while current is not None:
            cycle_length += 1
            current = current.next
            if current == slow:
                break
        return cycle_length

    def find_start_cycle(self, head, cycle_length):

        pointer1 = head
        pointer2 = head

        while cycle_length != 0:
            pointer2 = pointer2.next
            cycle_length -= 1

        while pointer1 != pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        return pointer1


node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

s = Solution()
print(s.detectCycle(node1))
