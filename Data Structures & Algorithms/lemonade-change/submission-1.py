class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        tens,fives =0,0
        for i in range(0, len(bills)):
            if bills[i] ==5:
                fives+=1
            elif bills[i]==10:
                tens+=1
                fives-=1
                if fives<0:
                    return False
            elif bills[i]==20:
                change = bills[i]-5
                if tens>0 and fives>0:
                    tens-=1
                    fives-=1
                elif fives>=3:
                    fives-=3
                else:
                    return False
        return True
        