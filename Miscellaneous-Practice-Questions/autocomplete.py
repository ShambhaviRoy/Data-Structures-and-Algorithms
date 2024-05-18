# Write code to implement autocomplete, look up words for a prefix (word)
# Assuming lookup only for lower case alphabets

class TrieNode:
    def __init__(self, text):
        self.text = text
        self.children = {}
        self.is_word = False

    
class Trie:
    def __init__(self):
        self.root = TrieNode('')  
    

    def insert_word(self, word):
        # insert word into Trie
        current_node = self.root
        for i, char in enumerate(word):
            if char not in current_node.children:
                prefix = word[0:i+1]
                current_node.children[char] = TrieNode(prefix)
            current_node = current_node.children[char]
        current_node.is_word = True


    def search_word(self, word):
        # search for word in trie
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return None
            current_node = current_node.children[char]
        if current_node.is_word:
            return current_node
        

    def starts_with(self, prefix):
        # given a prefix, find the possible words
        # iterate over trie to find prefix node
        # iterate thorugh list of subtrees and return a list of words
        words = []
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return []
            current_node = current_node.children[char]
        self.__child_words(current_node, words)
        return words


    def __child_words(self, node, words):
        if node.is_word:
            words.append(node.text)
        for letter in node.children:
            self.__child_words(node.children[letter], words)
            

    def size(self, current_node = None):
        if not current_node:
            current_node = self.root
        count = 1
        for letter in current_node.children:
            count += self.size(current_node.children[letter])
        return count



if __name__ == "__main__":

    words = ["and", "abc", "dad", "ant"]
    trie = Trie()

    for word in words:
        trie.insert_word(word)

    print(trie.search_word('par'))

    print(trie.starts_with('an'))

    print(trie.size())

        