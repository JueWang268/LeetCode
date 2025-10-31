class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        # ops = 0
        # target = [0] + target # to start
        # n = len(target)
        # curheight = 0
        # for i in range(1, n):
        #     if target[i - 1] < target[i]:
        #         # growth, carry over curheight
        #         diff = curheight
        #         # diff, grow curheight
        return target[0]+ sum([max(0, target[i] - target[i-1]) for i in range(1,len(target))])
