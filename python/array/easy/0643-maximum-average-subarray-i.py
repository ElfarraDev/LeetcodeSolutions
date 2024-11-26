class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        windowedSum = sum(nums[:k])
        maxSum = windowedSum

        for i in range(len(nums)-k):
            windowedSum = windowedSum - nums[i] + nums[i+k]
            maxSum = max(windowedSum,maxSum)

        return maxSum / k
