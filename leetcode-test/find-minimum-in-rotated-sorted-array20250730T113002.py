class Solution:
    def findMin(self, nums: List[int]) -> int:
        N = len(nums)
        lo = 0
        hi = N - 1
        if nums[0] < nums[N - 1]:
            return nums[0]

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if mid > 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]

            # if nums[mid] > nums[lo], it's on the "left" side,
            # min is to right
            if nums[lo] > nums[hi]:
                if nums[mid] >= nums[lo]:
                    lo = mid + 1
                    continue
                hi = mid - 1
                continue
            
            # else it's on the "right side", min is to left
            return nums[lo]
            
            # no scenario where nums[mid] < nums[lo] if nums[lo] < nums[hi]
            
        return nums[lo]