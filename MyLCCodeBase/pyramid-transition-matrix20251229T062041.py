class Solution:
    # @functools.lru_cache()
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        allowedpatterns = defaultdict(list)
        for a in allowed:
            allowedpatterns[a[:2]].append(a[2])
        # print(allowedpatterns)
        @functools.lru_cache(maxsize=None)
        def helper(base):
            print(f"helping {base}")
            if len(base) == 2 and base in allowedpatterns:
                return True
            
            n = len(base)
            candidates = []

            for i in range(n - 1):
                b = base[i:i+2]
                
                possible = allowedpatterns.get(b, [])
                if not possible:
                    return False

                candidates.append(possible)
            allcombs = []
            def dfs(cur, ind):
                if ind == len(candidates):
                    allcombs.append(cur)
                    return
                for k in candidates[ind]:
                    curn = cur + k
                    dfs(curn, ind+1)
                return
            dfs("", 0)
            # print(allcombs)

            for a in allcombs:
                if helper(a):
                    return True
            return False
        return helper(bottom)
                

            