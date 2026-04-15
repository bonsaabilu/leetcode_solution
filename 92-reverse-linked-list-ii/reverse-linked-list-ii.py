class Solution:
    def reverseBetween(self, head, left: int, right: int):
        if not head or left == right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Step 1: Move prev to (left-1)th node
        for _ in range(left - 1):
            prev = prev.next
        
        # Step 2: Reverse from left to right
        curr = prev.next
        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp
        
        return dummy.next