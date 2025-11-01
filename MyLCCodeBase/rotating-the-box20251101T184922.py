class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        n = len(boxGrid)
        m = len(boxGrid[0])
        rotated = [["."]*n for _ in range(m)]
        for i in range(n):
            s = m - 1 # next stone position
            for j in range(m-1, -1, -1):
                if boxGrid[i][j] == "*":
                    s = j - 1
                    rotated[j][n - 1-i] = "*"
                    continue
                if boxGrid[i][j] == "#":
                    rotated[s][n - 1-i] = "#"
                    s -= 1
        # for line in rotated:
        #     print(line)
        # # print(rotated)
        return rotated