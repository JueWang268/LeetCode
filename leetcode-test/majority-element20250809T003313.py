class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        candidate = nums[0]

        for n in nums:
            if n == candidate:
                count += 1
                continue
            count -= 1
            if count == 0:
                candidate = n
                count = 1
        return candidate