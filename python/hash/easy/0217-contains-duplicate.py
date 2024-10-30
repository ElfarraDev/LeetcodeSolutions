from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        lookup = Counter(nums)

        for key, value in lookup.items():
            if value > 1:
                return True

        return False
