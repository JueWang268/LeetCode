class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(dict)
        ans = []
        for i in range(len(equations)):
            x, y = equations[i]
            quotient = values[i]
            adj[x][y] = quotient
            adj[y][x] = 1/quotient
        
        def dfs(product, node, target, seen):
            # float, str, str, set
            if node in seen:
                return 0
            if target == node:
                return product
            
            seen.add(node)
            for neighbor in adj[node]:
                res = dfs(product*adj[node][neighbor], neighbor, target, seen)
                if res:
                    return res
            # seen.remove(node)
            return 0

        for v1, v2 in queries:
            if v1 not in adj or v2 not in adj:
                ans.append(-1)
                continue
            q = dfs(1, v1, v2, set())
            if q:
                ans.append(q)
                continue
            ans.append(-1)
        return ans

