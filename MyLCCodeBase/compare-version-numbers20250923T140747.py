class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        n = max(len(version1), len(version2))

        version1 = version1.split(".")
        version2 = version2.split(".")
        for i in range(n):
            if i >= len(version1):
                rev1 = 0
            else:
                rev1 = int(version1[i])
            if i >= len(version2):
                rev2 = 0
            else:
                rev2 = int(version2[i])
            if rev1 > rev2:
                return 1
            if rev1 < rev2:
                return -1
        return 0
            
