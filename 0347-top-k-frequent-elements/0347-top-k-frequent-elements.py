import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = collections.Counter(nums).most_common(k)
        result = list(val for val, count in dic)
        return result