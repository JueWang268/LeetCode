class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        ans = 0

        while l < r:
            ans = max(ans, min(height[l], height[r])*(r-l))
            if height[l] < height[r]:
                lh = height[l]
                while l < r and height[l] <= lh:
                    l += 1
                continue
            rh = height[r]
            while r > l and height[r] <= rh:
                r -= 1
        return ans