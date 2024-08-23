#Combination of 2Sum and 2Sum-2(sorted)
#First sort then set the first (base) number then for the remaining have a start and end pointer and if if the sum>0 resuce end pointer 
# and if the sum<0 increase start pointer and if sum == 0 add to output list.
# If the new base number == prev_base then continue as all the possibilites have been taken care of and to prevent duplicate.
# Also to increase speed when sum is 0 and list is added to output now the next start = start + 1 but here have a while loop so that 
# this start is not equal to previous start to imporve speed and avoid duplicate.




#Another soultion is:
#1. Sepertate nums into 3 set arrrays of pos, neg and zero.
# If len(zero) >=3 add [0,0,0] to output
#If len(0) >=1 and there are pos and neg complimentatr pairs add them to list eg.[-2,0,2]
# For all combinations of neg nos if there is a pos them add them to list 
# For all combinations of pos nos if there is a neg then add them to list 

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        n_nums = len(nums)
        for i in range(len(nums)-1):
            base = nums[i]
            
            if i>0 and base == nums[i-1]:
                continue
            start = i+1
            end = len(nums) - 1

            while start < end:

                sum_ = base + nums[start] + nums[end]
                if sum_ >0:
                    end = end -1
                elif sum_ <0:
                    start = start + 1
                elif sum_ == 0:
                    output.append([base,nums[start],nums[end]])
                    start = start +1
                    while nums[start] == nums[start-1] and start<end:
                        start = start + 1



        return output
       