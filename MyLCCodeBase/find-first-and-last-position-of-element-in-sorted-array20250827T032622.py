class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = bisect_left(nums, target)
        if left > len(nums) - 1 or nums[left] != target:
            return [-1, -1]
        return [left, bisect_right(nums, target) - 1]