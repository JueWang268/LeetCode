import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        hep = [(nums1[0]+nums2[0], 0, 0)]
        visited = set(hep)
        ans = []
        for i in range(min(k, len(nums1)*len(nums2))):
            cursum, a, b = heapq.heappop(hep)
            # print(f"{hep=}, {a=},{b=}, just popped {cursum}")
            ans.append([nums1[a],nums2[b]])
            # add new candidates
            if a + 1 < len(nums1) and (nums1[a+1]+nums2[b], a+1, b) not in visited:
                heapq.heappush(hep, (nums1[a+1]+nums2[b], a+1, b))
                visited.add((nums1[a+1]+nums2[b], a+1, b))
            if b + 1 < len(nums2) and (nums1[a]+nums2[b+1], a, b+1) not in visited:
                heapq.heappush(hep, (nums1[a]+nums2[b+1], a, b+1))
                visited.add((nums1[a]+nums2[b+1], a, 1+b))
        return ans
            

