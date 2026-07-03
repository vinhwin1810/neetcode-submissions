class MinStack:

    def __init__(self):
        # 0 2 1
        # getMin() => 0 1 2
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack:
            cur_min = self.min_stack[-1]
        else:
            cur_min = math.inf
        self.min_stack.append(min(val, cur_min))

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
