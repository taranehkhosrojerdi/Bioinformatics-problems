class TrieNode:
    def __init__(self, num):
        self.number = num
        self.children = [None] * 26
        self.eow = False


class Trie:

    def __init__(self):
        self.edges = {}
        self.num_of_nodes = 0
        self.root = self.getNode()
        self.num_of_nodes += 1

    def getNode(self):
        return TrieNode(self.num_of_nodes)

    def _charToIndex(self, ch):
        return ord(ch) - ord('A')

    def insert(self, key):
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
                self.num_of_nodes += 1
            self.edges[(pCrawl.number, pCrawl.children[index].number)] = key[level]
            pCrawl = pCrawl.children[index]
        pCrawl.eow = True


keys = []
with open('rosalind_ba9a.txt') as f:
    lines = f.readlines()
for line in lines:
    keys.append(line.replace('\n', ''))
t = Trie()
for key in keys:
    t.insert(key)
for key in t.edges.keys():
    print("{}->{}:{}".format(key[0], key[1], t.edges[key]))