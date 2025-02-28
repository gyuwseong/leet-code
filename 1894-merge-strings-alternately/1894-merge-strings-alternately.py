class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        start = 0
        for w in word1:
            result.append(w)
            if start < len(word2):
                result.append(word2[start])
                start += 1

        if start < len(word2):
            result.extend(word2[start:])

        return ''.join(result)
        