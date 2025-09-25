class Solution:
    @lru_cache(maxsize=5000)
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        if not s3:
            return True
        if not s1:
            return s2 == s3
        if not s2:
            return s1 == s3
        ptr1 = ptr2 = 0
        for i,letter in enumerate(s3):
            if s1[ptr1] != letter and s2[ptr2] != letter:
                return False
            if s1[ptr1] == letter:
                #! both letters the same
                if s2[ptr2] == letter:
                    return (self.isInterleave(s1[ptr1:], s2[ptr2+1:], s3[i+1:]) or 
                        self.isInterleave(s1[ptr1+1:], s2[ptr2:], s3[i+1:]))
                ptr1 += 1
                if ptr1 == len(s1):
                    return s2[ptr2 : ] == s3[i+1:]
                continue
            if s2[ptr2] == letter:
                ptr2 += 1
                if ptr2 == len(s2):
                    return s1[ptr1 : ] == s3[i+1:]
        return False