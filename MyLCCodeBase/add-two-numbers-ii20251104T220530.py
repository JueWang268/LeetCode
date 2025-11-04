# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = n2 = 0
        while l1:
            n1 *= 10
            n1 += l1.val
            l1 = l1.next
        while l2:
            n2 *= 10
            n2 += l2.val
            l2 = l2.next
        n = n1 + n2
        if n == 0:
            return ListNode(val=0)
        print(n)
        k = int(math.log10(n)) # digits for later
        dummy = ans = ListNode()
        for i in range(k, -1, -1):
            ans.next = ListNode(val = (n // 10**i)%10)
            ans = ans.next
        return dummy.next