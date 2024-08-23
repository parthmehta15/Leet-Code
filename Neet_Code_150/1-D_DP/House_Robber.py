'''
Similar to DP
Edge case if len(nums)<= 2 return max(nums)
Have another array to keep track of max poossible loot
Go in reverse range(n-2)
for current i add the value and max(nums[i+2:]) to data at that position

keep one and two like all dp problems


'''




class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return max(nums)
        one = nums[-1]
        two = nums[-2]
        data = [0]*len(nums)
        data[-1] = one
        data[-2] = two

        for i in reversed(range(len(nums)-2)):
            dummy = two
            two = nums[i] + max(data[i+2:])
            one = dummy
            data[i] = two

        return max(data[0], data[1])

        