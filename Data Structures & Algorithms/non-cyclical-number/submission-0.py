class Solution:
    def isHappy(self, n: int) -> bool:
        seta = set()
        while n not in seta:
            seta.add(n)
            n = self.get_num(n)
            if n == 1:
                return True
        return False

    
    def get_num(self,n):
        sumofs=0
        while n:
            digit = n%10
            sumofs +=digit**2
            n = n//10
        return sumofs

        