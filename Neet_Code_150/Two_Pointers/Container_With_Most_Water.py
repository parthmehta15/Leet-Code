#Initialize two pointer one at start and other at end. Calculate the water level and store in a variable. Loop till left<right
#Move the pointer with smaller height to right or left, recalualte the water level and if more than the previous then store the new value.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        pointer_1 = 0
        pointer_2 = len(height) - 1
        highest = 0

        while pointer_1 < pointer_2:
            water_stored = min(height[pointer_1], height[pointer_2]) * (pointer_2 - pointer_1)
            if water_stored > highest:
                highest = water_stored
            if height[pointer_1] >= height[pointer_2]:
                pointer_2 -= 1
            else:
                pointer_1 += 1
        return highest





# Brute Force slow solution

        # highest = 0
        # for i, j in enumerate(height):
        #     for k, l in enumerate(height):
        #         curr = min(j,l) * (k-i)
        #         if  curr > highest:
        #             highest = curr
        # return highest

