class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0
        dirs = [[1,0],[-1,0],[0,-1], [0, 1]]
        seen = set()
        def bfs(y,x):
            seen.add((y,x))
            for dx, dy in dirs:
                if (0 <= y+dy < m and 0 <= x + dx < n and 
                    grid[y+dy][x+dx] == "1" and not (y+dy, x+dx) in seen):
                    bfs(y+dy, x+dx)
            return

        for i in range(m):
            for j in range(n):
                if (i,j) not in seen and grid[i][j] == "1":
                    ans += 1
                    bfs(i,j)
        return ans