class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # zero_count = nums.count(0)

        # if zero_count > 1:
        #     return [0] * len(nums)

        # prod = 1
        # for num in nums:
        #     if num != 0:
        #         prod *= num

        # result = []
        # for num in nums:
        #     if zero_count == 1:
        #         result.append(prod if num == 0 else 0)
        #     else:
        #         result.append(prod // num)

        # return result


        n = len(nums)
        result = [1] * n

        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n-1,-1,-1):
            result[i] *= suffix
            suffix *= nums[i]

        return result
