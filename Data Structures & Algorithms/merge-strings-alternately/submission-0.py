class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1, l2 = 0,0
        string = ''
        while l1<len(word1) and l2<len(word2):
            string = string + word1[l1]+word2[l2]
            l1+=1
            l2+=1
        string = string+word1[l1:len(word1)]+word2[l2:len(word2)]
        return string