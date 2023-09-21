class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = nums[0]
        max_sum = nums[0]
        for i in nums[1:]:
            curr_sum = max(i, curr_sum+i)
            max_sum = max(max_sum, curr_sum)
        return max_sum


