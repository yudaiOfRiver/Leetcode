class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        elements = collections.defaultdict(lambda: 0)  # elements in the sliding window, index
        curMax = 0

        for i in range(len(s)):
            if s[i] in elements:
                for j in range(i-len(elements), elements[s[i]]+1):
                    del elements[s[j]]
            elements[s[i]] = i
            curMax = max(curMax, len(elements))

        return curMax
