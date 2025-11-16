class Solution:
    def numSub(self, s: str) -> int:
        i = 0
        n = len(s)
        cnt = defaultdict(int)
        ans = 0
        MOD = 10**9+7
        while i < n:
            streak = 0
            while i < n and s[i] == "1":
                streak += 1
                i += 1
            if streak:
                cnt[streak] += 1
            i += 1
        for l, freq in cnt.items():
            # l + l(l+1)/2
            if l == 1:
                ans += freq
                continue
            ans += freq * (l + l*(l-1)//2)%MOD 
        return ans % MOD