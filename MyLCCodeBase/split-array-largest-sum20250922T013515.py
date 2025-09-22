class Solution:
    

    def splitArray(self, weights: List[int], n: int) -> int:
        def can_divide(weights: List[int], n: int, max_weight: int) -> bool:
            """Check if we can split weights into <= n baskets without exceeding max_weight."""
            count = 1
            curr_sum = 0
            for w in weights:
                if curr_sum + w > max_weight:
                    count += 1
                    curr_sum = w
                    if count > n:
                        return False
                else:
                    curr_sum += w
            return True
        """Return the minimal possible largest basket weight."""
        left = max(weights)  # at least one basket must hold the heaviest apple
        right = sum(weights) # one basket holds everything

        while left < right:
            mid = (left + right) // 2
            if can_divide(weights, n, mid):
                right = mid  # try smaller max
            else:
                left = mid + 1  # need bigger max
        
        return left