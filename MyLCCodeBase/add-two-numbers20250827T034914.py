# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = l1
        b = l2
        carry = 0
        ans = ListNode()
        cur = ans
        while a or b or carry:
            summ = carry
            if a:
                summ += a.val
                a = a.next
            if b:
                summ += b.val
                b = b.next
            carry, summ = divmod(summ, 10)
            cur.next = ListNode(val = summ)
            cur = cur.next
        return ans.next
