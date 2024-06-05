import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        rt = collections.defaultdict(list)
        for w in strs:
            s_w = ''.join(sorted(w))
            rt[s_w].append(w)
        return(list(rt.values()))
        