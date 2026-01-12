class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        x1, y1 = points[0]
        time = 0
        for i in range(1,n):
            x2, y2 = points[i]
            hordist = abs(x1 - x2)
            verdist = abs(y1 - y2)
            smaldist = min(hordist, verdist)
            offset = max(hordist, verdist) - smaldist
            time += smaldist + offset
            
            x1, y1 = x2, y2
        return time