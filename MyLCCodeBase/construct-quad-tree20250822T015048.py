"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def quarters(self, grid):
        # return list of 4 small grids
        n = len(grid)
        dirs = [[0, 0], [0, n//2],[n//2, 0],  [n//2,n//2]]
        ans = []
        for dy, dx in dirs:
            curqu = []
            for i in range(dy, dy + n//2):
                newrow = []
                for j in range(dx, dx + n//2):
                    newrow.append(grid[i][j])
                curqu.append(newrow)
            ans.append(curqu)
        return ans

    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        # base case
        if n == 1:
            return Node(bool(grid[0][0]), True, None, None, None, None)
        # scans itself and see if its all equal

        for g in range(1, n*n):
            i, j = divmod(g - 1, n)
            y,x = divmod(g, n)
            if grid[i][j] != grid[y][x]:
                qs = self.quarters(grid)
                return Node(True, False, 
                    self.construct(qs[0]),
                    self.construct(qs[1]),
                    self.construct(qs[2]),
                    self.construct(qs[3])
                )
        
        return Node(bool(grid[0][0]), True, None,None,None,None )
