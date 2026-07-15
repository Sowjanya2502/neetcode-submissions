class StockSpanner:

    def __init__(self):
       self.stack1=[]
        

    def next(self, price: int) -> int:
        st = 1
        while self.stack1 and price >= self.stack1[-1][0]:
            
            st1= self.stack1.pop()
            st = st+st1[1]

        self.stack1.append([price,st])
        return self.stack1[-1][1]
        




# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)