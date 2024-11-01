from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = Counter(nums)
        majorityValue = -999999999
        majorityKey = 0

        for k,v in majority.items():
            if v > majorityValue:
                majorityValue = v
                majorityKey = k

        return majorityKey
