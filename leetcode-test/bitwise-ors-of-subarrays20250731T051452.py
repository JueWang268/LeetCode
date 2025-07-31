class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ans = set()
        cur = set(arr[:1])
        for a in arr:
            new_cur = set([a])
            for or_res in cur:
                new_cur.add(a | or_res)
            # print(f"{new_cur}")
            cur = new_cur
            ans |= cur
        return len(ans)