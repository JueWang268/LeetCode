class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        m = len(A)
        n = len(B)
        # A should be short
        if m > n:
            return self.findMedianSortedArrays(B,A)
        
        # search space
        left = 0
        right = m - 1

        while left <= right:
            partA = left + (right - left + 1)//2
            partB = (m + n + 1)//2 - partA # if total num add, might as well put middle to left
            # check if already middle
            maxLeftA = A[partA-1] if partA >= 0 else -1000001
            minRightA = A[partA] if partA < m else 1000001
            maxLeftB = B[partB - 1] if partB >= 0 else -1000001
            minRightB = B[partB] if partB < n else 1000001
            if maxLeftA > minRightB:
                # partA too large
                right = partA - 1
            elif maxLeftB > minRightA:
                left = partA + 1
            # return value
            if m + n % 2 == 1:
                return max(A[partA - 1], B[partB - 1])
            else:
                return (A[partA - 1] + B[partB - 1])/2
        return 0
