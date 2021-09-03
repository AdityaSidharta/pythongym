# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum_val = l1.val + l2.val
        if sum_val > 9:
            if l1.next is None:
                l1.next = ListNode(val=1)
            else:
                l1.next.val += 1
            sum_val -= 10
        if l1.next is None and l2.next is None:
            return ListNode(val=sum_val)
        elif l1.next is None:
            return ListNode(val=sum_val, next=self.addTwoNumbers(ListNode(), l2.next))
        elif l2.next is None:
            return ListNode(val=sum_val, next=self.addTwoNumbers(l1.next, ListNode()))
        else:
            return ListNode(val=sum_val, next=self.addTwoNumbers(l1.next, l2.next))

