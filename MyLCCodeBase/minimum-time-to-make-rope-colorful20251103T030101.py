import heapq
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        def findmin(a,b):
            return sum(neededTime[a:b]) - max(neededTime[a:b])

        ans = 0
        k = 0
        n = len(colors)
        while k < n:
            # want to match colors
            r = k + 1
            curmax = neededTime[k]
            cursum = neededTime[k]
            while r < n and colors[k] == colors[r]:
                cursum += neededTime[r]
                curmax = max(curmax, neededTime[r])
                r += 1
            if r > k + 1:
                # print(f"find min sum of {k}, {r}")
                ans += cursum-curmax
            k = r
        return ans