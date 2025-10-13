# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        # curmin = 10001
        hasValid = True
        while hasValid:
            hasValid = False
            for i in range(len(lists)):
                head = lists[i]
                if head:
                    hasValid = True
                    h.append(head.val)
                    lists[i] = head.next
        dummy = ListNode()
        d = dummy
        for num in sorted(h):
            dummy.next = ListNode(val=num)
            dummy = dummy.next
        return d.next
