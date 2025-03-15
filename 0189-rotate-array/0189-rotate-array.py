class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        q = collections.deque(nums)
        q.rotate(k)
        nums[:] = list(q)
        