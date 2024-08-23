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

