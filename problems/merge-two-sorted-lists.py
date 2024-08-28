class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2) -> ListNode:
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 == None and list2 == None:
            return None
        elif list1 == None:
            return list2
        elif list2 == None:
            return list1
        current = ListNode()
        head = current
        while list1 or list2:
            if list1 == None:
                current = list2
                return head
            if list2 == None:
                current = list1
                return head
            if current == None:
                return head
            
            else:
                if list1.val <= list2.val:
                    current.val = list1.val
                    current.next = list2 if list1.next == None else ListNode()
                    list1 = list1.next
                else: 
                    current.val = list2.val
                    current.next = list1 if list2.next == None else ListNode()
                    list2 = list2.next
            current = current.next


if __name__ == '__main__':
    sol = Solution()
    # v4 = ListNode(4)
    # v2 = ListNode(2, v4)
    # v1 = ListNode(1, v2)

    # l4 = ListNode(4)
    # l3 = ListNode(3, l4)
    # l1 = ListNode(1, l3)
    
    res = sol.mergeTwoLists(None, ListNode(0))
    while res:
        print(res.val)
        res = res.next