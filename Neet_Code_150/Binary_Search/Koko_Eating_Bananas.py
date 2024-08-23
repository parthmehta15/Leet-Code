# If no of hours = size of array then return max(array)
# Else you need to find the hours taken to eat all bananas with spped form 1 to max of array
# Best way to do is Binary Search, find mid and calculate hours if less than required then change right to mid - 1 and
# if hours more than required thanmove left to mid + 1


import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)
        else:
            piles.sort()
            left = 1
            right = piles[-1]
            res = right
            while left<=right :
                mid = int((left + right)/2)
                curr_sum = 0
                for j in piles:
                    curr_sum = curr_sum + math.ceil(j/mid)
                if curr_sum>h:
                    left = mid + 1
                elif curr_sum <= h:
                    res = min(res, mid)
                    right = mid - 1
           
            return res 





                