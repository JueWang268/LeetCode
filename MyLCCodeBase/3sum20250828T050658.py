class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        ret = []
        n = len(nums)
        i = 0
        while i < n:
            while 0 < i and nums[i - 1] == nums[i]:
                i += 1
                if i == n:
                    return ret
            if nums[i] > 0:
                return ret
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[j] + nums[k] == -nums[i]:
                    ret.append([nums[i],nums[j],nums[k]])
                    print(f"found new triplet ({[nums[i],nums[j],nums[k]]}), {j=} {k=}")
                    k -= 1
                if nums[j] + nums[k] > -nums[i]:
                    k -= 1
                    continue
                j += 1
                while j < k and nums[j - 1] == nums[j]:
                    j += 1
            i += 1
        return ret
                
            