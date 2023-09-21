# Hint:
'''
Sort based on all start elements
Define initial start, end. Loop through,  
if end >= next_start then end = max(end, next_end) 
else add [start, end] to output
At the end add [start, end] to output
'''



class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals = sorted(intervals, key=lambda x: x[0])
        out = []
        start = intervals[0][0]
        end = intervals[0][1]
        for i in intervals[1:]:
            if end >= i[0]:
                end = max(end,i[1])
            
            else:
                out.append([start,end])
                start = i[0]
                end = i[1]
        out.append([start,end])
        return out

'''
Another approach would be to directly make changes in the out 

'''

# Leet Code Website solution
# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:

#         intervals.sort(key=lambda x: x[0])

#         merged = []
#         for interval in intervals:
#             # if the list of merged intervals is empty or if the current
#             # interval does not overlap with the previous, simply append it.
#             if not merged or merged[-1][1] < interval[0]:
#                 merged.append(interval)
#             else:
#             # otherwise, there is overlap, so we merge the current and previous
#             # intervals.
#                 merged[-1][1] = max(merged[-1][1], interval[1])

#         return merged