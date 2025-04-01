class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        num1_idx = m - 1
        num2_idx = n - 1
        curr_idx = m + n - 1
        while num2_idx >= 0:
            if num1_idx >= 0 and nums1[num1_idx] > nums2[num2_idx]:
                nums1[curr_idx] = nums1[num1_idx]
                num1_idx -= 1
            else:
                nums1[curr_idx] = nums2[num2_idx]
                num2_idx -= 1
            curr_idx -= 1

        return nums1
        