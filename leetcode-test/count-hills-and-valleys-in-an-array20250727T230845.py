class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            if i == 0 or i == len(nums) - 1 or nums[i] == nums[i-1]:
                continue
            left = right = 0
            for j in range(i - 1, -1, -1):
                if nums[j] == nums[i]:
                    continue
                if nums[j] < nums[i]:
                    left = -1
                    break
                left = 1
                break
            for j in range(i + 1, len(nums)):
                if nums[j] == nums[i]:
                    continue
                if nums[j] < nums[i]:
                    right = -1
                    break
                right = 1
                break
            if left == right and right != 0:
                ans += 1
        return ans