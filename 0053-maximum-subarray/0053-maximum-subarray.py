class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]

        sums = [0] * len(nums)
        sums[0] = nums[0]

        for i in range(1, len(nums)):
            sums[i] = max(sums[i - 1] + nums[i], nums[i])

        return max(sums)
        