class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for s in strs:
            enc = enc+str(len(s))+'#'+s
        return enc
    def decode(self, s: str) -> List[str]:
        result=[]
        i = 0
        while i < len(s):
            j = i
            while s[j]!='#':
                j=j+1
            length = int(s[i:j])
            result.append(s[j+1:j+length+1])
            j = j+length+1
            i=j
        return result          
