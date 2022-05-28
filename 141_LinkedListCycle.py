# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#        self.val = x
#        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return None
        seen = set()  # set of nodes seen before
        cur = head
        while cur.next:
            if cur in seen:
                return True
            seen.add(cur)
            cur = cur.next
        return False
