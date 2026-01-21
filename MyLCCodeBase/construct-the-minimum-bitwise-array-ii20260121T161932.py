class Solution:
    # 3210
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = [0 for num in nums]
        for i in range(len(nums)):
            num = nums[i]
            if num % 2 == 0:
                ans[i] = -1
                continue
            binum = bin(num)[2:] # get rid of 0b
            bl = len(binum)
            # find first 0 to the right, and turn 
            # next 1 into 0
            expon = bl - 1
            for j in range(bl - 1, 0, -1):
                if binum[j] == '1' and binum[j-1] == '0':
                    expon = bl - 1 - j
                    break
            mask = 1 << expon
            ans[i] = nums[i] - mask
        return ans
