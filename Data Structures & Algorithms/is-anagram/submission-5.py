class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list1 = [0 for i in range(0,26)]
        if len(s)!=len(t):
            return False
        for i in range(0,len(s)):
            list1[ord(s[i]) - ord('a')] += 1
            list1[ord(t[i]) - ord('a')] -= 1
        for i in list1:
            if i!=0:
                return False
        return True