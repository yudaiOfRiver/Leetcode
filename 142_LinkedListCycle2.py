# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        seen = set()
        cur = head
        while cur.next:
            if cur in seen:
                return cur
            cur = cur.next
        return None