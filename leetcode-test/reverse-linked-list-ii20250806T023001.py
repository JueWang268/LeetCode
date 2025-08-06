# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dum = ListNode(next=head)
        if left == right:
            return head
        slow = dum
        fast = dum
        for i in range(left - 1):
            slow = slow.next
            fast = fast.next
        
        for i in range(right - left + 1):
            fast = fast.next
        print(f"{fast=}")
        
        prev = first = slow
        cur = second = slow.next
        while cur and prev != fast:
            print(f"{prev.val = } {cur.val = }")
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex
        first.next = prev
        second.next = cur
        return dum.next
