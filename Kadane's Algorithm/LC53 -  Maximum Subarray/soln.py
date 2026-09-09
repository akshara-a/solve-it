class Solution(object):
    def maxSubArray(self, nums):
        maximum = current = nums[0]

        for i in nums[1:]:
            current = max(i, current + i)
            maximum = max(maximum, current)

        return maximum
