class Solution(object):
    # actually a simple algorithm 
    # confounded with many many variables
    def findXSum(self, nums, k, x):
        res = []

        counts = defaultdict(int)
        for i in range(k):
            counts[nums[i]] += 1

        # Create a heap that moves the highest values to the top
        low = []

        for n, c in counts.items():
            heapq.heappush(low, (-c, -n))

        value = 0
        high = []
        high_nums = set()
        # putting the x most freq into highnums
        # (high frequency nums)
        while len(high_nums) < x and low:
            c, n = heapq.heappop(low)
            heapq.heappush(high, (-c, -n))
            high_nums.add(-n)
            value += c * n

        res.append(value)
        
        for i in range(k, len(nums)):
            leaving = nums[i - k]
            entering = nums[i]
            print(f"window: {i-k} to {i}")

            counts[leaving] -= 1
            counts[entering] += 1
            print(f"{leaving=}, {entering=}")

            if leaving in high_nums:
                print(f"highfreq num leaving, ")
                # heapq.heappush(high, (counts[leaving], leaving))
                value -= leaving

            # else:
            #     heapq.heappush(low, (-counts[leaving], -leaving))

            if entering in high_nums:
                heapq.heappush(high, (counts[entering], entering))
                value += entering
            else:
                heapq.heappush(low, (-counts[entering], -entering))

            # Lazily delete the lowest values from the high heap 
            # and highest values from low heap 
            # as long as they are not valid candidates.
            while high and (counts[high[0][1]] != high[0][0] or high[0][1] not in high_nums):
                heapq.heappop(high)

            while low and (counts[-low[0][1]] != -low[0][0] or -low[0][1] in high_nums):
                heapq.heappop(low)


            if low and high:
                # making sure the lowfreq numbers are still lower freq
                # if equal freq, make sure numerical value still smaller
                if -low[0][0] > high[0][0] or -low[0][0] == high[0][0] and -low[0][1] > high[0][1]:
                    new_count, new_high = heapq.heappop(low)
                    old_count, old_high = heapq.heappop(high)
                    high_nums.remove(old_high)
                    high_nums.add(-new_high)

                    value -= (old_high * counts[old_high])
                    value += (-new_high * counts[-new_high])
                    heapq.heappush(high, (-new_count, -new_high))
                    heapq.heappush(low, (-old_count, -old_high))

            while low and len(high_nums) < x:
                # add the low number into high numbers.
                new_count, new_high = heapq.heappop(low)
                value += (-new_high * counts[-new_high])
                heapq.heappush(high, (-new_count, -new_high))
                high_nums.add(-new_high)

            res.append(value)

        return res
