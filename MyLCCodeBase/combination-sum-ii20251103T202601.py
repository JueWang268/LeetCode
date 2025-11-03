class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        for i,c in enumerate(candidates):
            if c > target:
                candidates = candidates[:i]
                break
        
        def helper(start, path):
            print(f"start at index {start}, path: {path}")
            if sum(path) > target:
                return
            if sum(path) == target:
                ans.append(path[:])
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i]==candidates[i-1]:
                    # if candidates already considered on same depth
                    continue # skip, only the first is enough, the 
                    # subsequent numbers don't contribute
                path.append(candidates[i])
                helper(i+1, path)
                path.pop()
            return
        helper(0, [])
        return ans