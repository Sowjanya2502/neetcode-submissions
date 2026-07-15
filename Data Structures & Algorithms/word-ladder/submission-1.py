class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        dist = 0
        dictionary = set(wordList)
        if endWord not in dictionary:
            return 0
        if beginWord == endWord:
            return 1
        queue = deque([beginWord])
        visited = set([beginWord])
        while queue:
            for _ in range(len(queue)):
                curr_word = queue.popleft()
                if curr_word == endWord:
                    return dist+1
                for i in range(len(curr_word)):
                    for j in range(97,123):
                        new_word = curr_word[:i]+chr(j)+curr_word[i+1:]
                        if (new_word in dictionary and new_word not in visited):
                            visited.add(new_word)
                            queue.append(new_word)

            dist+=1
        return 0
            

