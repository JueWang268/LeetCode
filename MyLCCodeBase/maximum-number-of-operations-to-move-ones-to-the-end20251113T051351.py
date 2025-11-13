class Solution:
    def maxOperations(self, s: str) -> int:
        n = len(s)
        hasZero = False
        ans = 0
        prev = 0
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                hasZero = True
                continue
            # cur ans
            moves = int(hasZero) + prev
            prev = moves
            ans += moves
            # print(f"at position {i}, {s[i]=}, {ans=}")
            hasZero = False
        return ans