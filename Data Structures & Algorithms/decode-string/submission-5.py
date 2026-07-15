class Solution:
    def decodeString(self, s: str) -> str:
        op=''
        stack=[]
        for st in s:
            if st ==']':
                while stack[-1]!='[':
                    op = stack.pop()+op
                stack.pop()
                fre=''
                while stack and stack[-1].isdigit():
                    fre = stack.pop()+fre
                stack.append(op * int(fre))
                op=''
            else:
                stack.append(st)
        return ''.join(stack)

        