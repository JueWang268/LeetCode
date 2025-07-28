# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(val = -1, next = head)
        fast = dummy
        for i in range(n):
            fast = fast.next
        slow = dummy
        while fast and fast.next:
            fast = fast.next
            slow = slow.next
        print(f"{slow.val = }, {fast.val=}")
        slow.next = slow.next.next
        return dummy.next