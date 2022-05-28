from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        elements = defaultdict(lambda: 0)  # {elements:, number of appear}

        for c in s:
            elements[c] += 1
        
        for c in list(elements.keys()):
            if elements[c] == 1:
                return s.index(c)

        return -1