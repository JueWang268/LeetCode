class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = sum(piles)//h + int(sum(piles)%h != 0)
        hi = max(piles)
        piles.sort()
        while lo < hi:
            m = (hi - lo)//2 + lo
            
            # calculate time to eat up with m
            k = 0
            for p in piles:
                k += p // m + int(p % m != 0)
            # print(f"{m} bananas an hour, takes {k=} hrs")
            # based on k, adjust
            if k <= h:
                # too fast, decrease speed
                hi = m
                continue

            # too slow, increase speed
            lo = m + 1

            
        return lo