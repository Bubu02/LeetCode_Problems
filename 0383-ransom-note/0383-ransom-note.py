from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_counter = Counter(ransomNote)
        mag_counter = Counter(magazine)
        for char in ransom_counter:
            if ransom_counter[char] > mag_counter[char]:
                return False
        return True