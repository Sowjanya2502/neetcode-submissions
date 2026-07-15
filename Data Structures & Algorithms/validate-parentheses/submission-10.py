class Solution:
    def isValid(self, s: str) -> bool:
        se = []
        if len(s)==1:
            return False
        for i in range(len(s)):
            if s[i] in ['(', '{', '[']:
                se.append(s[i])
            elif s[i]==')':
                if len(se)==0 or se.pop() != '(':
                    return False
            elif s[i]=='}':
                if len(se)==0 or se.pop() != '{':
                    return False
            elif s[i]==']':
                if len(se)==0 or se.pop() != '[':
                    return False 
        return len(se)==0
