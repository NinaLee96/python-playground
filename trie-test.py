
class TrieNode:

    def __init__(self, char=""):
        self.char = char
        self.children = {}
        self.is_done = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode(char)
            node = node.children[char]
        node.is_done = True


    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_done

    def prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

t = Trie()
t.insert("hackathon")
t.insert("hack")
t.insert("hacker")
print(t.search('hack'))
print(t.prefix('ha'))
print(t.prefix('app'))


