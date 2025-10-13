# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        # initialize the heap
        for i,l in enumerate(lists):
            if l:
                heapq.heappush(h, (l.val, i, l))
        
        # build new list
        dummy = ListNode()
        tail = dummy
        while h:
            value, index, node = heapq.heappop(h)
            tail.next = node
            tail = tail.next
            if node.next:
                heapq.heappush(h, (node.next.val, index, node.next))
        return dummy.next