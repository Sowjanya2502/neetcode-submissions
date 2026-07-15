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
        return self.search_helper(0, word, node)
    def search_helper(self, wordindex: int, word: str, node:TrieNode())-> bool:
        for i in range(wordindex, len(word)):
            c = word[i]
            if c == '.':
                for child in node.children.values():
                    if self.search_helper(i+1, word, child):
                        return True
                return False
            else:
                if c not in node.children:
                    return False
                node = node.children[c]
        return node.is_word


        
