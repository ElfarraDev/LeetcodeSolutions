
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()

        for nums in nums1:
            if nums in nums2:
                result.add(nums)

        return [num for num in result]
