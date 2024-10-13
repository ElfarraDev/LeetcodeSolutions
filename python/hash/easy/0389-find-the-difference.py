from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        original = Counter(s)
        modified = Counter(t)

        for key, value in modified.items():
            if value > original[key]:
                return key

        return ""
