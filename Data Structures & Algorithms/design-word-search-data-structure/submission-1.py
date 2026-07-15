class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c]=TrieNode()
            node = node.children[c]
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self.root
        return self.dfs(0,word,node)
    def dfs(self, windex: int, word: str, node: TrieNode())->bool:
        for i in range(windex, len(word)):
            if word[i]=='.':
                for child in node.children.values():
                    if self.dfs(i+1, word, child):
                        return True
                return False
            else:
                if word[i] not in node.children:
                    return False
                node = node.children[word[i]]
        return node.is_word