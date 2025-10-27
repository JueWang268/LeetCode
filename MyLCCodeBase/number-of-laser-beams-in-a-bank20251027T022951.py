class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prevlights = 0

        ans = 0
        for floor in bank:
            if "1" not in floor:
                continue
            
            curlights = len([1 for room in floor if room == "1"])
            ans += curlights * prevlights
            prevlights = curlights
        return ans
            