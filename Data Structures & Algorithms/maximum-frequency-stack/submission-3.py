class FreqStack:

    def __init__(self):
        self.count1=defaultdict(int)
        self.stacks=defaultdict(list)
        self.max_freq=0

    def push(self, val: int) -> None:
        self.count1[val]+=1
        self.max_freq=max(self.max_freq, self.count1[val])
        self.stacks[self.count1[val]].append(val)

    def pop(self) -> int:
        mapvalue = self.stacks[self.max_freq].pop()
        self.count1[mapvalue]-=1
        if len(self.stacks[self.max_freq])==0:
            self.max_freq-=1
        return mapvalue
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()