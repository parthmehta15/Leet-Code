# Slower solution finds the max height on all left and all right side, finds the min of those max 
# and subtracts it with height at current position. If < 0 then water_content is 0. Do this for all heights.
# This only has 1 pointer.

# In the faster solution there are 2 pointer one left at the start and one right at the end.
# There are 2 variables left_max and right_max. Now with while left<right find height at all positions.
# If left_max < right_max then increase the left pointer by 1 else reduce right pointer by 1 
# and for this position find the water content by min(left_max, right_max) - curr_height (at left or right depending on which one just moved).
# This works because and we do not miss out any positions because, the water level at first and last positions is 0 
# and there needs to be atleast 1 element between left and right pointer.




## With 2 pointers O(1) memory O(n) time
class Solution:
    def trap(self, height: List[int]) -> int:
        
        water_content = 0
        left_max = height[0]
        right_max = height[-1]
        left = 0 
        right = len(height)-1

 

        while left < right:
           
            if left_max <= right_max:
                left = left + 1
                water_level = min(left_max, right_max) - height[left]
                if height[left]>left_max:
                    left_max = height[left]
                if water_level>0:
                    water_content += water_level
                else:
                    continue
                    
            if left_max > right_max:
                right = right - 1
                water_level = min(left_max, right_max) - height[right]
                if height[right]>right_max:
                    right_max = height[right]

                if water_level>0:
                    water_content += water_level
                else:
                    continue

 
        return water_content






## Without 2 pointers O(n) memory O(n) time
# class Solution:
#     def trap(self, height: List[int]) -> int:
        # water_content = 0
        # for i,level in enumerate(height):
        #     if i == 0 or i == len(height)-1:
        #         continue
        #     left = height[:i]
        #     left_max = max(left)
        #     right = height[i+1:]
        #     right_max = max(right)
        #     water = min(left_max, right_max) - level
        #     if water < 0: water = 0
        #     water_content = water_content + water
        # return water_content


                    


            
            

