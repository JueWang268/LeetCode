class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        # enumerate every possible sidelength val
        MOD = 10**9+7
        hFences.sort()
        vFences.sort()
        ans = -1
        hvals = set()
        hFences = [1] + hFences + [m]
        vFences = [1] + vFences + [n]
        hl = len(hFences)
        vl = len(vFences)

        for i in range(hl - 1):
            for j in range(i + 1, hl):
                hvals.add((hFences[j] - hFences[i]) % MOD)
        # print(list(hvals))

        for i in range(vl - 1):
            for j in range(i+1, vl):
                gap = (vFences[j] - vFences[i]) % MOD
                if gap in hvals:
                    ans = max(ans, gap)
        if ans == -1:
            return -1
        return (ans**2) % MOD