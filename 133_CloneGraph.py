"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node):
        if not node:
            return None

        old_to_new = {} # {origin: copy}

        def clone(n):
            if n in old_to_new.keys():
                return old_to_new[n]

            copy = Node(n.val)
            old_to_new[n] = copy

            for nei in n.neighbors:
                copy.neighbors.append(clone(nei))

            return copy

        return clone(node)
