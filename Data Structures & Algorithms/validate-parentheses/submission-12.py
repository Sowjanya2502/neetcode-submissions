class Solution:
    def isValid(self, s: str) -> bool:
        map1={'(':')','{':'}', '[':']'}
        stack1=[]
        for st in s:
            if st in map1:
                stack1.append(st)
            else:
                if stack1 and map1[stack1[-1]]==st:
                    stack1.pop()
                else:
                    return False
                
        return True if not stack1 else False
        
        