class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_cnt = 0
        nums_set = set(nums)

        for num in nums_set:
            if num - 1 not in nums_set:
                cnt = 1
                curr = num
                while curr + 1 in nums_set:
                    curr += 1
                    cnt += 1
                max_cnt = max(cnt, max_cnt)
        return max_cnt
        