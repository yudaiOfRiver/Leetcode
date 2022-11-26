class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        def oper(symble, i, j):
            if symble == "+":
                return i + j
            elif symble == "-":
                return i - j
            elif symble == "*":
                return i * j
            else:
                return i // j

        operands = ["+", "-", "*", "/"]

        stack = []
        for t in tokens:
            print(stack)
            if t in operands:
                j = stack.pop()
                i = stack.pop()
                res = oper(t, int(i), int(j))
                stack.append(res)
            else:
                stack.append(t)

        return stack[0]

tokens = ["4","-2","/","2","-3","-","-"]
obj = Solution()
print(obj.evalRPN(tokens))
