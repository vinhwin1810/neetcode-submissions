class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        fast = head
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next

        steps = length // k
        dummy = ListNode()
        tail = dummy
        cur = head

        for _ in range(steps):
            prev = None
            group_start = cur
            for _ in range(k):
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            tail.next = prev
            tail = group_start
        
        tail.next = cur
        
        return dummy.next