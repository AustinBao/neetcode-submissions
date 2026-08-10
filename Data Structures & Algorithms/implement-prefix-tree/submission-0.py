class TrieNode:
    def __init__(self):
        self.children = {}  
        self.is_end_of_word = False  


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # Start at the root node
        node = self.root
        # Traverse through each character of the word
        for char in word:
            # If the character is not in the current node's children, add it
            if char not in node.children:
                node.children[char] = TrieNode()
            # Move to the next node (child)
            node = node.children[char]
        # After the loop, mark the node as the end of the word
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        # Start at the root node
        node = self.root
        # Traverse through each character of the word
        for char in word:
            # If the character is not in the current node's children, return False
            if char not in node.children:
                return False
            # Move to the next node (child)
            node = node.children[char]
        # After traversing all characters, check if we're at the end of a word
        return node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        # Start at the root node
        node = self.root
        # Traverse through each character of the prefix
        for char in prefix:
            # If the character is not in the current node's children, return False
            if char not in node.children:
                return False
            # Move to the next node (child)
            node = node.children[char]
        # If we traverse through all characters of the prefix, return True
        return True
        
        