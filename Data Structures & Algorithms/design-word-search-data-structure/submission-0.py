class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to hold child nodes
        self.is_end_of_word = False  # Boolean to mark end of word


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()  # Initialize the root of the Trie

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            # If the character is not in the current node's children, add it
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        # After the loop, mark the node as the end of the word
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        # Helper function for DFS search
        def dfs(node, i):
            # Base case: if we've checked all characters in the word
            if i == len(word):
                return node.is_end_of_word

            char = word[i]

            # If the current character is '.', we must check all possible child nodes
            if char == '.':
                for child in node.children.values():
                    if dfs(child, i + 1):  # Check the next character in all children
                        return True
                return False
            else:
                # If the character is not in the current node's children, return False
                if char not in node.children:
                    return False
                # Move to the next character
                return dfs(node.children[char], i + 1)

        # Start DFS from the root node with index 0
        return dfs(self.root, 0)