class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        ns, ne = newInterval
        ans = []
        if len(intervals) < 1:
            return [newInterval]
        while intervals[i][1] < ns:
            ans.append(intervals[i])
            i += 1
            if i == len(intervals):
                return intervals + [newInterval]
            # skipping all intervals that end
            # before new one even starts
        # now we got a problem.
        # need to insert
        if intervals[i][0] > ne:
            ans.append(newInterval)
            return ans + intervals[i:]
        # overlap. need to modify and then insert
        actual_ns = min(ns, intervals[i][0])
        actual_ne = max(ne, intervals[i][1])
        merged = [actual_ns, actual_ne]
        # ans.append(merged)

        # go through the rest
        i += 1
        while i < len(intervals):
            if intervals[i][0] > actual_ne:
                # completely clear, append rest
                return ans + [merged] + intervals[i:]
            merged[1] = max(merged[1], intervals[i][1])
            i += 1

        return ans + [merged]