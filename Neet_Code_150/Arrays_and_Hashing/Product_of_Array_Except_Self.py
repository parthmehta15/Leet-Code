#Hint: Take care of cases with zeros
#Keep a track of zeros 
#if no_zeros > 1 then all output zeros
#if no zeros the multiply all and divide by no
#if 1 zero then everthing zero except that term (multiply all other terms except zero)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        zeros = []
        tot_prod = 1

        for i in range(len(nums)):
            if nums[i] == 0:
                zeros.append(i)
            else:
                tot_prod = tot_prod * nums[i]
        
        print(tot_prod)
        if len(zeros)>1:
            out = [0]*len(nums)
        elif len(zeros) == 0:
            out = []
            for i in nums:
                out.append(int(tot_prod/i))
        else:
            out = [0]*len(nums)
            out[zeros[0]] = tot_prod

        return out
 


      