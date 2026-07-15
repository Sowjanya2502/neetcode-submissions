class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        st = ''
        num = ''
        for t in s:
            if t == ']':
                st = ''
                num = ''
                while stack and stack[-1]!='[':
                    st = stack.pop()+st                   
                stack.pop()
                while stack and stack[-1].isdigit():
                    num = stack.pop()+num
                st = st*int(num)
                stack.append(st)
            else:
                stack.append(t)
        return ''.join(stack)
