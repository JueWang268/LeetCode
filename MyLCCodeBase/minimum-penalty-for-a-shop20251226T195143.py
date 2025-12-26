class Solution:
    def bestClosingTime(self, customers: str) -> int:
        penalty = [0 for i in range(len(customers) + 1)]
        Ncount = 0
        for i in range(len(customers)):
            if customers[i] == "N":
                Ncount += 1
            penalty[i+1] += Ncount
        Ycount = 0
        for i in range(len(customers)-1, -1, -1):
            if customers[i] == "Y":
                Ycount += 1
            penalty[i] += Ycount
        
        
        return penalty.index(min(penalty))
        