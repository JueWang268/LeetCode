class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        if len(nums) < 2:
            return 0
        return min(nums[i+k-1] - nums[i] for i in range(len(nums) - k + 1))

            