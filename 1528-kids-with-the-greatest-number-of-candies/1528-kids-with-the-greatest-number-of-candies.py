class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        maxCandies = max(candies)
        return [candy + extraCandies >= maxCandies for candy in candies]