class Solution:
    def closeStrings(self, word1, word2):
        # Different lengths → cannot be close
        if len(word1) != len(word2):
            return False

        # Both strings must contain the same characters
        if set(word1) != set(word2):
            return False

        # Character frequencies must have the same multiset
        return sorted([word1.count(c) for c in set(word1)]) == \
               sorted([word2.count(c) for c in set(word2)])