class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        def simulate(idx, direc, nums):
            # print(f"simulation begins with {idx=} and {direc=}")
            l = sum(nums[:idx]) if idx > 0 else 0
            r = sum(nums[idx+1:]) if idx < len(nums)-1 else 0
            # lets say 2 0 1, dir -1, ok
            # 2 0 1 with 1, no.
            # 1 0 1 whatever
            if abs(l-r) > 1:
                return False
            if l-r == 0:
                return True
            if l-r == -direc:
                return True
            return False
        ans = 0
        i = 0
        while i < len(nums):
            curscore = 0
            if nums[i] == 0:
                curscore = int(simulate(i, 1, nums[:]))+int(simulate(i, -1, nums[:]))
                ans += curscore
                while i < len(nums)-1 and nums[i+1] == 0:
                    ans += curscore
                    i += 1
            i += 1
        return ans
