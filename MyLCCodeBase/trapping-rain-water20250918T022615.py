class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 1:
            return 0
        # two pass
        # left bound for each space
        # right bound for each space
        leftb = [0 for h in height]
        rightb = [0 for h in height]
        lm = height[0]
        for i in range(1, len(height)):
            leftb[i] = lm
            lm = max(lm, height[i])
        rm = height[-1]
        ans = 0
        for i in range(len(height) - 2, -1, -1):
            ans += max(min(rm, leftb[i]) - height[i], 0)
            rm = max(rm, height[i])
        return ans

