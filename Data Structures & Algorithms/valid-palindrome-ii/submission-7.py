class Solution:
    def isPalindrome(self,s:str):
        l,r=0,len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True
    def validPalindrome(self, s: str) -> bool:
        i,j=0,len(s)-1
        while i<j:
            if s[i]!=s[j]:
                 return self.isPalindrome(s[i+1:j+1]) or self.isPalindrome(s[i:j])
            i+=1
            j-=1
        return True
        