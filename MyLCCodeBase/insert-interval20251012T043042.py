class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ptr = 0
        ns, ne = newInterval
        merged_start = merged_end = -1
        n = len(intervals)
        res = []
        for ptr in range(n):
            start, end = intervals[ptr]
            if ns >= end:
                break
            