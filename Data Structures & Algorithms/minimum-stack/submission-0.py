class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_m = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.stack_m:
            self.stack_m.append(val)
        else:
            n_m = min(val, self.stack_m[-1])
            self.stack_m.append(n_m)

    def pop(self) -> None:
        self.stack.pop()
        self.stack_m.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack_m[-1]
        
