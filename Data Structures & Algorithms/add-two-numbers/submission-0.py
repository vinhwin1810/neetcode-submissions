# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        new_head = dummy

        while l1 or l2:
            if l1:
                val1 = l1.val
                l1 = l1.next
            else:
                val1 = 0
            if l2:
                val2 = l2.val
                l2 = l2.next
            else:
                val2 = 0

            new_val = val1 + val2 + carry
            if new_val > 9:
                carry = 1
            else:
                carry = 0
            new_node = ListNode(new_val % 10)
            new_head.next = new_node
            new_head = new_head.next
        if carry:
            new_node = ListNode(1)
            new_head.next = new_node
    

        return dummy.next