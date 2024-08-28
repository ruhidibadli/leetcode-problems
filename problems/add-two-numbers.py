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
        
        dummy = ListNode(0)
        tail = dummy
        carry = 0

        while l1 is not None or l2 is not None or carry !=0:
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0

            sum = val1 + val2 + carry

            new_val = sum % 10
            carry = sum // 10

            newNode = ListNode(new_val)
            tail.next = newNode
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        result = dummy.next
        dummy.next = None
        return result
            

