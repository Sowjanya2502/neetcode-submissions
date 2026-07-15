class Solution:
    def isPalindrome(self, s: str) -> bool:
        str=""
        for i in s.lower():
            if i.isalnum() is True:
                str = str+i
        l=0
        r=len(str)-1
        count =0
        while l<=r :
            if str[l] != str[r]:
                return False
            l += 1
            r -= 1
        return True;