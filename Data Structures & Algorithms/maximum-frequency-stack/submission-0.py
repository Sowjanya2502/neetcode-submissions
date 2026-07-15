class FreqStack:

    def __init__(self):
        self.stack1 =[]
        self.mp1 = defaultdict(int)
        self.mp2 = defaultdict(list)
        self.max_freq = 0
    def push(self, val: int) -> None:
        freq = self.mp1[val] + 1
        self.mp1[val]=freq
        self.mp2[freq].append(val)
        self.max_freq=max(self.max_freq,freq)
    def pop(self) -> int:
        val = self.mp2[self.max_freq].pop()
        self.mp1[val]-=1
        if not self.mp2[self.max_freq]:
            self.max_freq -= 1
        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()