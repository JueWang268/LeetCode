class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        monstk = []
        heights = [0] + heights + [0]
        n = len(heights)
        res = 0
        for i in range(n):
            curh = heights[i]
            # print(f"\ni={i}, height={curh}")
            # print(f"Stack before while: {monstk}")
            while monstk and heights[monstk[-1]] > curh:
                # start popping these bars, their days are over
                lastind = monstk.pop()
                w = i - 1 - monstk[-1] 
                h = heights[lastind]
                res = max(res, w*h)
                # print(f"  Popped: height={heights[monstk[-1]]}, started_at={monstk[-1]}")
                # print(f"  Width calculation: i({i}) - started_at({monstk[-1]}) - 1= {w}")
                # print(f"  Area: {w} × {h} = {w*h}")
                # print(f"  Current max: {res}")
            monstk.append(i)
        return res
    
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        maxarea = 0
        heights = [0 for x in range(n)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    heights[j] += 1
                    continue
                heights[j] = 0
            maxarea = max(maxarea, self.largestRectangleArea(heights))
        return maxarea