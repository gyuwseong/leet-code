class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        if set(word1) != set(word2):
            return False
        word1_hash = sorted(collections.Counter(word1).values())
        word2_hash = sorted(collections.Counter(word2).values())
        if word1_hash != word2_hash:
            return False
        return True