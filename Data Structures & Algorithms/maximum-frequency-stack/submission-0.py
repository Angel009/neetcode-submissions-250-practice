class FreqStack:

    def __init__(self):
        self.count = {}
        self.max_count = 0
        self.stacks = {}

    def push(self, val: int) -> None:
        val_count = 1 + self.count.get(val, 0)
        self.count[val] = val_count

        if val_count > self.max_count:
            self.max_count = val_count
            self.stacks[val_count] = []
        
        self.stacks[val_count].append(val)

    def pop(self) -> int:
        ans = self.stacks[self.max_count].pop()
        self.count[ans] -= 1

        if not self.stacks[self.max_count]:
            self.max_count -= 1
        
        return ans
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()