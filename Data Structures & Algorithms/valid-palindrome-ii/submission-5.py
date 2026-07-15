class Solution:
    def palindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        while l<=r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True
    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        while l<=r:
            if s[l]!=s[r]:
                return self.palindrome(s[l+1:r+1]) or self.palindrome(s[l:r])
            l+=1
            r-=1
        return True
    

