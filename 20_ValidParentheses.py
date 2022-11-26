class Solution:
    def isValid(self, s: str) -> bool:
        pair = {'(': ')',
                '{': '}',
                '[': ']'}

        stack = []
        for i in range(len(s)):
            si = s[i]
            if si in pair.keys():
                stack.append(si)
            elif stack == [] or si != pair[stack.pop()]:
                return False

        if not stack:
            return True
        else:
            return False

s = "(){}}{"
obj = Solution()
print(obj.isValid(s))
