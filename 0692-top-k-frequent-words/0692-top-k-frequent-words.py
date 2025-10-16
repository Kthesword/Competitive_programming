class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.freq = 0

class Trie():
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True
        node.freq += 1
    
    def collect(self, node=None, prefix="", result=None):
        if result is None:
            result = []
        if node is None:
            node = self.root
        if node.is_end:
            result.append((prefix, node.freq))
        for ch in sorted(node.children.keys()):
            self.collect(node.children[ch], prefix + ch, result)
        return result

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        all_words = trie.collect()
        all_words.sort(key=lambda x: (-x[1], x[0]))
        return [w for w, _ in all_words[:k]]