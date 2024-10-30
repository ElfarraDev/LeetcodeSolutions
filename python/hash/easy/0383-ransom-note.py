from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran = Counter(ransomNote)
        mag = Counter(magazine)

        for key,value in ran.items():
            if key not in mag or mag[key] < value:
                return False

        return True
