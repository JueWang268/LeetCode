class SegmentTree:
    def __init__(self, xs):
        # xs: sorted list of unique x-coordinates
        self.xs = xs
        n = len(xs)
        self.cnt = [0] * (4 * n)  # count of active rectangles covering this segment
        self.total = [0] * (4 * n)  # total covered length in this segment
        
    def update(self, idx, left, right, ql, qr, val):
        # [ql, qr] is the query interval in compressed coordinates
        # val is +1 for OPEN, -1 for CLOSE
        
        # If current segment doesn't overlap with query
        if qr <= self.xs[left] or ql >= self.xs[right]:
            return
            
        # If current segment is completely covered by query
        if ql <= self.xs[left] and self.xs[right] <= qr:
            self.cnt[idx] += val
        else:
            # Partial overlap - recurse
            mid = (left + right) // 2
            self.update(idx * 2, left, mid, ql, qr, val)
            self.update(idx * 2 + 1, mid, right, ql, qr, val)
            
        # Update total covered length for this segment
        if self.cnt[idx] > 0:
            # Completely covered
            self.total[idx] = self.xs[right] - self.xs[left]
        else:
            # Partially covered or not covered
            if right - left == 1:
                self.total[idx] = 0
            else:
                self.total[idx] = self.total[idx * 2] + self.total[idx * 2 + 1]
    
    def query(self):
        # Returns total covered length across entire x-range
        return self.total[1]

class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        # Step 1: Collect all unique x-coordinates
        xs = set()
        events = []
        
        for x1, y1, x2, y2 in rectangles:
            xs.add(x1)
            xs.add(x2)
            events.append((y1, 1, x1, x2))  # OPEN event
            events.append((y2, -1, x1, x2))  # CLOSE event
        
        # Step 2: Sort x-coordinates and events
        xs = sorted(xs)
        events.sort()
        
        # Step 3: Initialize segment tree
        seg_tree = SegmentTree(xs)
        
        # Step 4: Sweep line
        result = 0
        prev_y = events[0][0]
        
        for y, typ, x1, x2 in events:
            # Add area of the strip: width * height
            width = seg_tree.query()
            height = y - prev_y
            result += width * height
            result %= MOD
            
            # Update segment tree
            seg_tree.update(1, 0, len(xs) - 1, x1, x2, typ)
            prev_y = y
        
        return result % MOD