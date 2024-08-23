#Faster approach using 2 pointers, so in this case have pointers to start and end. Next in a while loop till start<end or
# even works till True. See if numbers[start], numbers[end] add up to target else if <target then start+1 else if >target then end-1.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        start = 0
        end = len(numbers) - 1
        while True:
            if numbers[start] + numbers[end] == target:
                return [start+ 1, end + 1]

            elif numbers[start] + numbers[end] > target:
                end = end - 1
            elif numbers[start] + numbers[end] < target:
                start = start + 1


# Slower approach where you find the difference by sub target from all nums. Then for all nos search if they lie in numbers list and 
# return the two index added by 1. also have a conditon that if both index are same return next index because there are same numbers.

# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         diff = []
#         for i in numbers:
#             diff.append(target - i)
#         for i in range(len(diff)):
#             if diff[i] in numbers:
#                 if i== numbers.index(diff[i]):
#                     return [i+1, numbers.index(diff[i])+2]
#                 else:
#                     return [i+1, numbers.index(diff[i])+1]