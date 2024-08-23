# Using Binary search
# Set res to left most.
#While left<right
# if left < right that means that part of arrray is sorted and upadate res with left most element.
# or find mid, compare with res
# If mid num >= left_num that means search in right array hence left = mid + 1
# else search in left array hence right = mid - 1


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0 
        right = len(nums)-1
        res= nums[left]

        while left<= right:
            if nums[left]< nums[right]:
                res = min(res, nums[left])
                break
            mid = int((left + right)/2)
            res = min(res, nums[mid])

            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1

        return res







# #Slow solution as rotated array in Python does not make much sense
# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         return min(nums)