# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        if head is None:
            return None
        elif head.next is None:
            return head.val
        else:
            curr = head
            num = ""
            while curr is not None:
                num += str(curr.val)
                curr = curr.next

        return int(num, 2)