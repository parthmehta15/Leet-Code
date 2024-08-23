#Faster Using Binary Search

#Find no of elements in each array and also total elements
# We need to just find half numbers on the left side of combined array so find half length
# Assign the smaller array a and other b
# start binary search while True -> cos will get output in the loop only
# Find mid_a and mid_b = half_len - mid_a - 2 (-2 due to 0 index)
# Now mid_a is a_left and mid_a+1 is a_right 
# Now mid_b is b_left and mid_b+1 is b_right 
# Take care of edge cases so that its not out of bound by assiging flaot('+-inf')
# if a_left < b_right and b_left < a_right that mens left side is correct 
# so return avg of max(a_left,b_left) and  min(a_right, b_right) if total elements even 
# else if total elements odd return min(a_right, b_right)
# Else if a_left > b_right then right = mid - 1
# Else left = mid + 1



class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n_len1 = len(nums1)
        n_len2 = len(nums2)
        total_len = (n_len1 + n_len2)
        half_len = (n_len1 + n_len2) // 2


        if n_len1 <= n_len2:
            a = nums1
            b = nums2
        else:
            a = nums2
            b = nums1

        left = 0
        right = len(a) -1 
        while True:
            mid = (left + right) // 2
            left_b_idx = half_len - mid -2
            
            a_left = a[mid] if mid >= 0 else float('-inf')
            a_right = a[mid + 1] if mid + 1 < len(a) else float('inf')

            b_left = b[left_b_idx] if left_b_idx>= 0 else float('-inf')
            b_right = b[left_b_idx + 1] if left_b_idx + 1 < len(b) else float('inf')

            if a_left <= b_right and b_left <= a_right:
                if total_len%2 == 0:
                    left_max =  max(b_left,  a_left)
                    right_min =  min(b_right,  a_right)
                    return (left_max + right_min)/2 
                else:
                    return min(b_right,  a_right)
            elif a_left > b_right:
                right = mid - 1
            else:
                left = mid + 1
 




# # Using Python 
# # Without Binary Search -> pretty fast

# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         merge = nums1 + nums2
#         merge.sort()
#         n_elements = len(merge)
#         if n_elements%2 == 0:
#             return (merge[int(n_elements/2)] + merge[int(n_elements/2) - 1])/2

#         else:
#             return merge[int(n_elements/2)]
        