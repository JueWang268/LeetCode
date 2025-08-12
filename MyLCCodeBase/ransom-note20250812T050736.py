class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = Counter(magazine)
        ran = Counter(ransomNote)
        for let, freq in ran.items():
            if let not in mag or ran[let] > mag[let]:
                return False
        return True
