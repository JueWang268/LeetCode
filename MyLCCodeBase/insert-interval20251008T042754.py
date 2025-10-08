class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ptr = 0
        ns, ne = newInterval
        merged_start = merged_end = -1
        n = len(intervals)
        res = []
        for start, end in intervals:
            if ns <= end:
                if ne < start:
                    # no need to merge at all
                    res.append(newInterval)
                    while ptr < n:
                        res.append(intervals[ptr])
                        ptr += 1
                    return
                # start merging
                merged_start = min(ns, start)
                merged_end = max(ne, end)
                res.append([merged_start, merged_end])
                ptr += 1
                break
            ptr += 1
            

        if merged_start == -1:
            return intervals + [newInterval]
        while ptr < n: 
            res.append(intervals[ptr])
            ptr += 1
        return res