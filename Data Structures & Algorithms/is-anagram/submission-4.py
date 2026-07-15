class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list1 = [0 for i in range(0,26)]
        list2 = [0 for i in range(0,26)]
        if len(s)!=len(t):
            return False
        for i in range(0,len(s)):
            list1[ord(s[i]) - ord('a')] += 1
            list2[ord(t[i]) - ord('a')] += 1
        if list1 == list2:
            return True
        return False