class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack1=[]
        for t in tokens:
                if t == '+':        
                    stack1.append((stack1.pop()+stack1.pop()))
                elif t == '-':
                    a=stack1.pop()
                    b=stack1.pop()
                    stack1.append(b-a)
                elif t == '*':
                    stack1.append(stack1.pop()*stack1.pop())
                elif t=='/':
                    a=stack1.pop()
                    b=stack1.pop()
                    stack1.append(int((b)/a))
                else:
                    stack1.append(int(t))
        return stack1[0]