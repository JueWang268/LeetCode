class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = set()
        deltas = [[1,0], [-1,0], [0, 1], [0,-1]]
        def recur(r, c, w):
            # print(f"looking at [{r}, {c}] ({board[r][c]}) with {w}, {seen}")
            if len(w) == 0:
                return True
            for dy, dx in deltas:
                if (r + dy, c + dx) in seen:
                    continue
                if -1 < r + dy < M and -1 < c + dx < N and board[r + dy][c + dx] == w[0]:
                    # print(f"got letter {w[0]}")
                    seen.add((r+dy, c + dx))
                    if recur(r+dy, c+dx, w[1:]):
                        return True
                    seen.remove((r+dy, c + dx))
            return False

        M = len(board)
        N = len(board[0])
        for i in range(M):
            for j in range(N):
                if board[i][j] == word[0]:
                    seen.add((i,j))
                    if recur(i, j, word[1:]):
                        return True
                    seen.remove((i,j))
        return False
        