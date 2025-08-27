class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        inddict = defaultdict(list)
        for i in range(len(nums)):
            inddict[nums[i]].append(i)
        for i,num in enumerate(nums):
            comp = target - num
            if comp in inddict:
                for ind in inddict[comp]:
                    if ind != i:
                        return [i, ind]
        return None