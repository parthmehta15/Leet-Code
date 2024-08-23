#Similar to prev problem 
# Use binary search 
# While left < = right
# If mid == target return mid
# If leftmost< mid :
    # if target > mid then go right or target < leftmost go right:
        # left = mid + 1
    #else target < mid and target > leftmost
        # right = mid - 1
# Else rightmost > mid:
    # if target < mid or target > rightmost:
        # right = mid - 1
    #else target > mid or target < rightmost:
        # left = mid + 1




class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1
        while left <= right:
            mid = int((left + right)/2)
            if nums[mid] == target:
                return mid
            
            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                     left = mid + 1

        return - 1