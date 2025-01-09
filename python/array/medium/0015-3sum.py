class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        nums.sort()

        for i in range(len(nums)):
            ptr1 = i + 1
            ptr2 = len(nums) - 1

            if nums[i] > 0 or nums[ptr2] < 0:
                break

            while ptr1 < ptr2:
                target = nums[i] + nums[ptr1] + nums[ptr2]
                if target == 0:
                    if (nums[i],nums[ptr1],nums[ptr2]) not in seen:
                        seen.add((nums[i],nums[ptr1],nums[ptr2]))
                    ptr1 += 1
                elif target > 0:
                    ptr2 -= 1
                else:
                    ptr1 += 1

        return [values for values in seen]
