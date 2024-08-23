
## Dictionary:

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data = {}
        for i in range(len(nums)):
            num = target - nums[i]
            if num in data:
                return [i,data[num]]
            data[nums[i]] = i






#Brute Force
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i,j
