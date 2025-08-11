class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freqs = defaultdict(int)
        l = 0
        r = 0
        ans = 0
        while r < len(nums):
            freqs[nums[r]] += 1
            while freqs[nums[r]] > k:
                # shrink
                freqs[nums[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
            r += 1
        return ans