class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                # Pop two numbers from the stack
                num2 = stack.pop()
                num1 = stack.pop()

                # Apply the operator
                if token == "+":
                    stack.append(num1 + num2)
                elif token == "-":
                    stack.append(num1 - num2)
                elif token == "*":
                    stack.append(num1 * num2)
                elif token == "/":
                    # Note: Convert to int for floor division
                    stack.append(int(num1 / num2)) 
            else:
                # Token is a number, push onto stack
                stack.append(int(token))

        # The result is the last element in the stack
        return stack.pop()