class Node:
    def __init__(self, c = None):
        self.c = c
        self.end = False
        self.d = defaultdict(Node)

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.d:
                curr.d[char] = Node(char)                
            curr = curr.d[char]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.d:
                return False
            curr = curr.d[char]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.d:
                return False
            curr = curr.d[char]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)