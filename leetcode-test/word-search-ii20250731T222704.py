from collections import defaultdict
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ans = []
        def backtrack(r, c, parent):
            letter = board[r][c]
            cur = parent[board[r][c]]

            # base case: at end of a word
            if '$' in cur:
                ans.append(cur['$'])
                # no longer relevant, del to save time
                del cur['$']
            
            dirs = [(1,0),(-1,0),(0,1),(0,-1)]
            board[r][c] = "X"
            for dy, dx in dirs:
                if (0 <= r+dy < m and 0 <= c + dx < n
                    and board[r+dy][c+dx] in cur):
                    backtrack(r+dy, c+dx, cur)
            board[r][c] = letter

            # final clean-up
            # shear the leaves?
            if not cur:
                del parent[letter]
            return

        trie = dict()
        for word in words:
            t = trie
            for letter in word:
                t = t.setdefault(letter, {})
            t["$"] = word
        
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    backtrack(i, j, trie)


        return ans