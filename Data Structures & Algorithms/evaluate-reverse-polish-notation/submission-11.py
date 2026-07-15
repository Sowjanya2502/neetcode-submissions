class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in ['+', '-', '*','/']:
                stack .append(tokens[i])
            elif tokens[i] == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(a)+int(b))
            elif tokens[i] == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b)-int(a))
            elif tokens[i] == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(a)*int(b))
            elif tokens[i]=='/':
                a = int(stack.pop())
                b = int(stack.pop())
                if (a==0) or (b==0):
                    stack.append(0)
                else:
                    stack.append(int(int(b)/int(a)))
        return int(stack[-1])