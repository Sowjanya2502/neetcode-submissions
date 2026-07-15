class MinStack:

    def __init__(self):
        self.s1 = []

    def push(self, val: int) -> None:
        self.s1.append(val)

    def pop(self) -> None:
        self.s1.pop()

    def top(self) -> int:
        return self.s1[-1]

    def getMin(self) -> int:
        min_length = float('inf')
        for i in range(len(self.s1)):
            min_length = min(min_length, self.s1[i])
        return min_length
