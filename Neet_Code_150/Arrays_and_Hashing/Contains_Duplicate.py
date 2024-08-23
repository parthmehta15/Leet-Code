# Using Set

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a = len(nums)
        b = len(set(nums))
        if a == b:
            return False
        else:
            return True


#Using Dictionary (Faster, More Memory)
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         data = {}
#         for i in nums:
#             if i in data:
#                 return True
#             else:
#                 data[i] = 0
#         return False

#Using sorting (Slower than Dict, Less Memory)
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         nums = sorted(nums)
#         a = nums[0]
#         for i in nums[1:]:
#             if i == a:
#                 return True
#             else:
#                 a = i
#         return False
