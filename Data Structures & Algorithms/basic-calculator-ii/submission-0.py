class Solution:
    def calculate(self, s: str) -> int:
        # if int => stack( if stack and stack[-1] in */ => calculate and append to stack)
        # elif +- => stack.append(+- int)
        # elif */ => stack.append(op)
        stack = []
        i = 0
        sign = 1
        num = 0
        while i < len(s):
            if s[i].isdigit():
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                
                if stack and stack[-1] in "*/":
                    op = stack.pop()
                    if op == "*":
                        prev = int(stack[-1]) * num
                    else:
                        prev = int(int(stack[-1]) / num)
                    stack.pop()
                    stack.append(str(prev))
                else:
                    stack.append(str(num * sign))
                    sign = 1
                num = 0
                i -= 1
            elif s[i] == "+":
                sign = 1
            elif s[i] == "-":
                sign = -1
            elif s[i] in "*/":
                stack.append(s[i])
            i += 1
        res = 0
        for num in stack:
            res += int(num)
        return res
