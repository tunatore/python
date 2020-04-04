# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if l1 is None and l2 is None:
            return None

        list_merged = []

        while l1 is not None and l1.val is not None and \
                l2 is not None and l2.val is not None:
            if l1.val < l2.val:
                list_merged.append(l1.val)
                l1 = l1.next
            elif l1.val == l2.val:
                list_merged.append(l1.val)
                list_merged.append(l2.val)
                l1 = l1.next
                l2 = l2.next
            else:
                list_merged.append(l2.val)
                l2 = l2.next

        while l1 is not None and l1.val is not None:
            list_merged.append(l1.val)
            l1 = l1.next

        while l2 is not None and l2.val is not None:
            list_merged.append(l2.val)
            l2 = l2.next

        l_ret = ListNode(list_merged.pop(0))
        head = l_ret
        while not len(list_merged) == 0:
            l_ret.next = ListNode(list_merged.pop(0))
            l_ret = l_ret.next
        return head


s = Solution()

l1 = ListNode(None)
l2 = ListNode(0)

print(s.mergeTwoLists(l1, l2))