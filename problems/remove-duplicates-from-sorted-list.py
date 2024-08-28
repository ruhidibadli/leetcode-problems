# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        head_node = None
        val_list = []

        while(head):
            if not head.val in val_list:
                if not head_node:
                    head_node = ListNode(head.val)
                    current = head_node
                else:
                    current.next = ListNode(head.val)
                    current = current.next
                val_list.append(head.val)
            head = head.next
        return head_node

if __name__ == '__main__':
    sol = Solution()
    v3 = ListNode(3)
    v33 = ListNode(3, v3)
    v4 = ListNode(2, v33)
    v2 = ListNode(1, v4)
    v1 = ListNode(1, v2)

    # l4 = ListNode(4)
    # l3 = ListNode(3, l4)
    # l1 = ListNode(1, l3)
    
    res = sol.deleteDuplicates(v1)
    while res:
        print(res.val)
        res = res.next