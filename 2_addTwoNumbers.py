# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # index -1
        cur = dummy
        curry = 0
        while l1 or l2 or curry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            cur.next = ListNode((v1 + v2 + curry) % 10)
            curry = (v1 + v2 + curry ) // 10
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next