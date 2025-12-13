
class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        ans = {"electronics": [], "grocery": [], "pharmacy": [], "restaurant": []}
        final = []
        
        N = len(code)
        def valcode(c):
            if not c:
                return False
            for l in c:
                if not (l.isalnum() or l == "_"):
                  return False
            return True

        for i in range(N):
            if valcode(code[i]) and businessLine[i] in ans and isActive[i]:
                ans[businessLine[i]].append(code[i])

        for c in sorted(ans["electronics"]):
            final.append(c)
        for c in sorted(ans["grocery"]):
            final.append(c)
        for c in sorted(ans["pharmacy"]):
            final.append(c)
        for c in sorted(ans["restaurant"]):
            final.append(c)
        
        return final