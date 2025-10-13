class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        if m == 1:
            return matrix[0]
        if n == 1:
            return [matrix[i][0] for i in range(m)]
        ans = []
        for i in range(min(m,n)//2):
            # from [0 + i, 0 + i] to [0 + i,n - 2 - i]
            for j in range(i, n - 1 - i):
                ans.append(matrix[i][j])
            # from [0 + i, n - 1 - i] to [m - 2 - i, n - 1 - i]
            for j in range(i, m - 1 - i):
                ans.append(matrix[j][n-1-i])
            # from [m - 1 - i, n - 1 - i] to [m - 1 - i, 1 + i]
            for j in range(n - 1 - i, i, -1):
                ans.append(matrix[m-1-i][j])
            # from [m - 1 - i, 0 + i] to [1 + i, 0 + i]
            for j in range(m - 1 - i, i, -1):
                ans.append(matrix[j][i])
        

        if min(m,n) % 2 == 1:
            # if m is smallest
            if m < n:
                ans.extend(matrix[m//2][m//2 : n - m//2])
                return ans
            # n smallest
            for i in range(n//2, m - n//2):
                ans.append(matrix[i][n//2])
        
        return ans
