class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        hashmap = defaultdict(list)
        for strng in strs:
            hashmap[tuple(sorted([let for let in strng]))].append(strng)
        return list(hashmap.values())
        