class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        m = len(A)
        n = len(B)
        # A should be short
        if m > n:
            return self.findMedianSortedArrays(B,A)
        
        # search space
        left = 0
        right = m

        while left <= right:
            partA = (left + right) //2 
            partB = (m + n + 1)//2 - partA # if total num odd, might as well put middle to left
            # print(f"left is {left}, {A[left] = }")
            print(f"{partA = } and {partB = }")
            # print(f"right is {right}")
            # check if already middle
            maxLeftA = A[partA-1] if partA > 0 else -1000001
            minRightA = A[partA] if partA < m else 1000001
            maxLeftB = B[partB - 1] if partB > 0 else -1000001
            minRightB = B[partB] if partB < n else 1000001
            if maxLeftA > minRightB:
                # partA too large
                print()
                right = partA - 1
                print(f'''
{maxLeftA =}
{minRightA=} 
{maxLeftB =}
{minRightB=} 
                ''')
                continue
            if maxLeftB > minRightA:
                left = partA + 1
                continue
            
            # return value
            if (m + n) % 2 == 1:
                print(f'''
{maxLeftA =}
{minRightA=} 
{maxLeftB =}
{minRightB=} 
                ''')
                return max(maxLeftA, maxLeftB)
            else:
                return ( max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2
        return 0
