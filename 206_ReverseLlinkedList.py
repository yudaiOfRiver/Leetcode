# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        else:
            stack = []
            cur = head
            while cur:
                stack.append(cur.val)
                cur = cur.next
            
            rev_head = ListNode(stack.pop())
            rev_cur = rev_head
            while stack:
                rev_cur.next = ListNode(stack.pop())
                rev_cur = rev_cur.next
            return rev_head
                
                
        