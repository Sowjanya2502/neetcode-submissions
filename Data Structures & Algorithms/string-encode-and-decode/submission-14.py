class Solution:

    def encode(self, strs: List[str]) -> str:
        enc_str = ""
        for s in strs:
            enc_str=enc_str+str(len(s))+"#"+s
        return enc_str

    def decode(self, s: str) -> List[str]:
        i,j = 0,0
        res=[]
        while i<len(s):
            while s[j]!="#":
                j+=1
            length=int(s[i:j])
            res.append("".join(s[j+1:j+length+1]))
            j=j+length+1
            i=j
        return res


