class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums) - 1
        lo = 0
        hi = n
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if target == nums[mid]:
                return mid
            # see if mid is on same side
            if nums[mid] >= nums[lo]:
                print("mid unrotated")
                if nums[mid] > target >= nums[lo]:
                    hi = mid - 1
                    continue
                lo = mid + 1
                continue
            # nums[mid] < nums[lo]

            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
                continue

            hi = mid - 1

        if nums[lo] == target:
            return lo
        return -1

