from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        products.sort()

        root = TrieNode()

        # Build Trie
        for product in products:
            node = root

            for ch in product:
                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]

                # Keep only 3 lexicographically smallest products
                if len(node.suggestions) < 3:
                    node.suggestions.append(product)


        result = []
        node = root

        for ch in searchWord:

            if node is not None and ch in node.children:
                node = node.children[ch]
                result.append(node.suggestions)
            else:
                node = None
                result.append([])

        return result