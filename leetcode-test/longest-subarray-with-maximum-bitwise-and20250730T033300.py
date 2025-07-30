class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 1
        streak = 1
        curmax = nums[0]
        for i,num in enumerate(nums):
            if num == curmax and i > 0 and nums[i - 1] == num:
                streak += 1
                ans = max(ans, streak)
                continue
            if i > 0 and nums[i - 1] != num:
                streak = 1
            # new big number
            if num > curmax:
                ans = 1
                curmax = num

        return ans