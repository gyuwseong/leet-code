class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
            def binarySearch(nums, target, is_left):
                start = 0
                end = len(nums) - 1
                idx = -1
                while start <= end:
                    mid = (start + end) // 2
                    if nums[mid] < target:
                        start = mid + 1
                    elif nums[mid] > target:
                        end = mid - 1
                    else:
                        idx = mid
                        if is_left:
                            end = mid - 1
                        else:
                            start = mid + 1
                return idx

            left = binarySearch(nums, target, True)
            right = binarySearch(nums, target, False)
            return [left, right]