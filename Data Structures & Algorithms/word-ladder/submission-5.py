class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset = set(wordList)
        visited=set()
        if beginWord==endWord:
            return 1
        if endWord not in wordset:
            return 0
        queue = deque([beginWord])
        visited = set([beginWord])
        dist=0
        while queue:
            for _ in range(len(queue)):
                curr_word = queue.popleft()
                if curr_word ==endWord:
                    return dist+1
                for i in range(len(curr_word)):
                    for j in range(97,123):
                        word = curr_word[:i]+chr(j)+curr_word[i+1:]
                        if (word in wordset) and (word not in visited):
                            visited.add(word)
                            queue.append(word)
            dist+=1
        return 0
