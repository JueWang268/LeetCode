class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # Longest increasing Subsequence strikes again
        n = len(strs[0])
        s = len(strs)
        dp = [1 for f in range(n)]
        for i in range(n):
            for j in range(i):
                lexorder = True
                for k in range(s):
                    # if every letter <= curr
                    if strs[k][j] > strs[k][i]:
                        lexorder = False
                        break
                if lexorder:
                    dp[i] = max(dp[i], dp[j] + 1)
        return n - max(dp)