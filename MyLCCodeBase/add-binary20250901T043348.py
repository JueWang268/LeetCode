class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        ans = ""
        # get long str
        long = b
        short = a
        if len(a) > len(b):
            long = a
            short = b
        diff = len(long) - len(short)
        for i in range(len(long) - 1, -1, -1):
            ld = int(long[i])
            if diff > i:
                sd = 0
            else:
                sd = int(short[i - diff])
            if carry:
                ans = str(int(not sd^ld)) + ans
                carry = sd | ld
                continue
            ans = str(sd^ld) + ans
            carry = sd & ld
        if carry:
            ans = "1" + ans
        return ans