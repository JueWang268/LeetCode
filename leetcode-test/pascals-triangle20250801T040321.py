class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows):
            newrow = []
            for j in range(i+1):
                if j == 0 or j == i:
                    newrow.append(1)
                    continue
                # print(f"{i}, {j}, {newrow=}, {ans=}")
                newrow.append(ans[i - 1][j-1] + ans[i - 1][j])
            ans.append(newrow)
        return ans