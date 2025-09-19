class Solution:
    def romanToInt(self, s: str) -> int:
        symb_tbl = {"I":1
            , "V":5
            , "X":10
            , "L":50
            , "C":100
            , "D":500
            , "M":1000
        }
        n = len(s)
        intgr = 0
        for i in range(n - 1):
            if symb_tbl[s[i+1]] <= symb_tbl[s[i]]:
                intgr += symb_tbl[s[i]]
                continue
            intgr -= symb_tbl[s[i]]

        return intgr + symb_tbl[s[n-1]]