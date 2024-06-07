import collections
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        ct = collections.defaultdict(int)
        words = [word for word in re.sub(r'\W', ' ', paragraph).lower().split() if word not in banned]
        for w in words:
            ct[w] += 1

        return max(ct, key=ct.get)