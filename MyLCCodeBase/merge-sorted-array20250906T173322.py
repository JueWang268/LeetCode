class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # go backward
        onepos =  m - 1
        twopos = n - 1
        ptr = len(nums1) - 1
        while onepos > -1 and twopos > -1:
            if nums1[onepos] > nums2[twopos]:
                nums1[ptr] = nums1[onepos]
                onepos -= 1
                ptr -= 1
                continue
            nums1[ptr] = nums2[twopos]
            twopos -= 1
            ptr -= 1
        # put the rest of nums2 in nums1
        while twopos > -1 and ptr > -1:
            