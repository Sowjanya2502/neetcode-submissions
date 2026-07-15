class FreqStack:

    def __init__(self):
        self.count1={}
        self.stacks=defaultdict(list)
        self.max_freq=0

    def push(self, val: int) -> None:
        valcount = 1+self.count1.get(val,0)
        self.count1[val] = valcount
        if valcount>self.max_freq:
            self.max_freq = valcount
        self.stacks[valcount].append(val) 

    def pop(self) -> int:
        a=self.stacks[self.max_freq].pop()
        self.count1[a]-=1
        if not self.stacks[self.max_freq]:
            self.max_freq-=1
        return a

        
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()