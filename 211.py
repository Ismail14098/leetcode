class Node:
    def __init__(self, c = None):
        self.c = c
        self.end = False
        self.d = defaultdict(Node)

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.d:
                curr.d[char] = Node(char)                
            curr = curr.d[char]
        curr.end = True

    def search(self, word: str) -> bool:
        def recursion(node: Node, i: int, word: str):
            if i == len(word):
                return node.end
            if word[i] == '.':
                for next in node.d:
                    if recursion(node.d[next], i+1, word):
                        return True
                return False
            elif word[i] in node.d:
                if recursion(node.d[word[i]], i+1, word):
                    return True
                return False
        return recursion(self.root, 0, word)
                


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)