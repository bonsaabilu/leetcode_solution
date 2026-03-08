# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Helper function to reverse nodes between start and end
        def reverse(start: ListNode, end: ListNode) -> ListNode:
            prev, curr = None, start
            while curr != end:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            # Find the kth node ahead
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next   # ✅ return linked list head

            group_next = kth.next
            start = group_prev.next
            end = kth.next

            # Reverse the group
            new_group_head = reverse(start, end)

            # Connect reversed group back
            group_prev.next = new_group_head
            start.next = group_next
            group_prev = start
