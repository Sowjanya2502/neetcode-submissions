class Solution:
    def isValid(self, s: str) -> bool:
        map={')':'(', '}':'{', ']':'['}
        lst = []
        for c in s:
            if c not in map:
                lst.append(c)
                continue
            if not lst or lst[-1]!=map[c]:
                return False
            lst.pop()
        return not lst
