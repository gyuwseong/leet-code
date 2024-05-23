import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = prices[0]
        max_prof = 0

        for p in prices[1:]:
            max_prof = max(max_prof, p - min_p)
            min_p = min(min_p, p)
        return max_prof