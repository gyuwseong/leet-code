import collections

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = collections.defaultdict(int)
        length = len(nums) / 2

        for num in nums:
            dic[num] += 1
            if dic[num] > length:
                return num
        