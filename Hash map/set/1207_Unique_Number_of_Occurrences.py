from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr):
        freq = Counter(arr)

        return len(freq.values()) == len(set(freq.values()))