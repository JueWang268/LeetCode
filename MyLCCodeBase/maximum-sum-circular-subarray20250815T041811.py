class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Kadane for both max and min
        # min is as negative as possible
        # if there's a min then max is just on both ends

        globalmax = -30001
        curmax = -30001
        gmin = 30001
        cmin = 30001
        cutind = 0 # cutoff index

        n = len(nums)
        for i in range(n):
            curmax = max(curmax + nums[i], nums[i])
            cmin = min(nums[i] + cmin, nums[i])
            globalmax = max(curmax, globalmax)
            gmin = min(gmin, cmin)
        
        snums = sum(nums)
        if snums == gmin:
            return globalmax
        
        return max(globalmax, snums-gmin)