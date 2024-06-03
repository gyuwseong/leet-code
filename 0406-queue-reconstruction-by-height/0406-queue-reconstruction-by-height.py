class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []
        for ppl in people:
            heapq.heappush(heap, [-ppl[0], ppl[1]])

        result = []
        while heap:
            ppl = heapq.heappop(heap)
            result.insert(ppl[1], [-ppl[0], ppl[1]])
        return result
