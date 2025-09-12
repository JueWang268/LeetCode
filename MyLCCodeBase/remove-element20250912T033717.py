class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i = 0
        k = 0
        while i < n:
            # equal
            if nums[i] == val:
                i += 1
                continue
            nums[k] = nums[i]
            
            k += 1
            i += 1
        return k