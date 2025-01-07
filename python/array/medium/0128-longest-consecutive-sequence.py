class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = 0
        numSet = set(nums)

        for num in numSet:
            curr_length = 1

            if num - 1 not in numSet:
                curr = num

                while curr + 1 in numSet:
                    curr += 1
                    curr_length += 1

                length = max(length,curr_length)

        return length
