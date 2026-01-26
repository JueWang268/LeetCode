class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mindiff = 10**6+1
        al = []
        for i in range(len(arr) - 1):
            a = arr[i]
            b = arr[i + 1]
            if b - a == mindiff:
                al.append([a,b])
            elif b - a < mindiff:
                mindiff = b-a
                al = [[a,b]]
        return al
            