class Solution:
    @lru_cache(maxsize = 1000)
    def isMatch(self, s: str, p: str) -> bool:
        DEBUG = False

        if s == p:
            return True
            # everything before the ?* should be perfect
        k = 0
        if DEBUG:
            print(f"checking {s} with {p}")
        for i in range(len(s)):
            # rule out all letters first
            if i >= len(p):
                return False
            if i + 1 < len(p) and p[i+1] == "*":
                k = i+1
                break
            if p[i] == ".":
                continue
            if p[i].isalpha() and p[i] != s[i]:
                return False
                    
        if k == 0:
            # no stars matching given s length segment
            # check if p ends with ?*
            if len(s) < len(p):
                if (len(p) - len(s)) % 2 == 1:
                    # you can't get to 0 with odd number characters
                    return False 
                p_leftover = p[len(s):]
                if DEBUG:
                    print(f"{p_leftover=}")
                for i in range(1, len(p_leftover), 2):
                    if p_leftover[i] != "*":
                        return False
                return True
            return True
        
        if k + 1 < len(p):
            pattern_suffix = p[k+1:]
        else:
            pattern_suffix = ""
        starred_letter = p[k-1]
        if self.isMatch(s[k-1:], pattern_suffix):
            return True
        if starred_letter == "." or starred_letter == s[k-1]:
            for i in range(1, 20):
                if self.isMatch(s[k-1:], starred_letter*i + pattern_suffix):
                    return True
        return False
        
