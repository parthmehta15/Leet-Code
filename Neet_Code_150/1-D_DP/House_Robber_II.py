'''

# Same as house rober 1, since there is circle divide the array into 2 subarrays
# One wich does not have first element and one which does not have last element 
# Run house robber 1 code and then find the max of both answers
# You can also write it as a function 
# Final answer is basically a max of 4 values: first 2 values of both sub-arrays

'''



class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=3:
            return max(nums)

        new_nums = nums[1:]
        one = new_nums[-1]
        two = new_nums[-2]
        data = [0]*len(new_nums)
        data[-1] = one
        data[-2] = two

        for i in reversed(range(len(new_nums)-2)):
            dummy = two
            two = new_nums[i] + max(data[i+2:])
            one = dummy
            data[i] = two

        max1 = max(data[0], data[1])


        new_nums2 = nums[:-1]
        one2 = new_nums2[-1]
        two2 = new_nums2[-2]
        data2 = [0]*len(new_nums2)
        data2[-1] = one2
        data2[-2] = two2

        for i in reversed(range(len(new_nums2)-2)):

            dummy = two2
            two2 = new_nums2[i] + max(data2[i+2:])
            one2 = dummy
            data2[i] = two2

        max2 = max(data2[0], data2[1])
            
        return max(max1, max2)
        # return max(data2[0], data2[1], data[0], data[1])
        