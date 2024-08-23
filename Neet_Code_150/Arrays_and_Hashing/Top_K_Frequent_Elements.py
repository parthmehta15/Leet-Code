class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data = {}
        output = []
        for i in nums:
            data[str(i)] = data.get(str(i),0) + 1
        data = sorted(data.items(), key=lambda x:x[1], reverse = True)
        for i in data[:k]:
            output.append(int(i[0]))
        return output

        # Other way to sort the dict is to have another list where we save list of elements index as count and then loop through them to add till k 


# #Other Solution
# from collections import Counter
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
#         # O(1) time 
#         if k == len(nums):
#             return nums
        
#         # 1. build hash map : character and how often it appears
#         # O(N) time
#         count = Counter(nums)   
#         # 2-3. build heap of top k frequent elements and
#         # convert it into an output array
#         # O(N log k) time
#         return heapq.nlargest(k, count.keys(), key=count.get) 