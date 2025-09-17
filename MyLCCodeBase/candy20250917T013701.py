class Solution:
    def candy(self, ratings: List[int]) -> int:
        # transform rating to simple comparisons
        # min = 1
        # if child has better rating, get one more candy
        N = len(ratings)
        distr = [1 for r in ratings]
        # two passes
        # first make sure all children better than left get more candies
        for i in range(1, N):
            if ratings[i] > ratings[i - 1]:
                distr[i] = distr[i - 1] + 1
        # then do a right to left pass
        # keeping values if they are already satisfied
        ans = distr[N-1]
        for i in range(N - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                distr[i] = max(distr[i], distr[i+1]+1)
            ans += distr[i]
        return ans