
# wrong, probably
class Trie:

    def __init__(self):
        self.word_set = set()

    def insert(self, word: str) -> None:
        self.word_set.add(word)

    def search(self, word: str) -> bool:
        return word in self.word_set

    def startsWith(self, prefix: str) -> bool:
        for word in self.word_set:
            if word.startswith(prefix):
                return True
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)