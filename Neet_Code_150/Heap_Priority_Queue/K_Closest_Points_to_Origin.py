
'''
Slightly slow, use heaps 
Can ignore sqrt

Append all to list and then use heapify rather than heappush for all elements

Also pop minimum vales and add to new list

'''


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist_array = []
        for i in points:
            dist = ((i[0]**2) + (i[1]**2))
            dist_array.append((dist, i))
        
        heapq.heapify(dist_array)
        result = []
        while k >0:
            result.append(heapq.heappop(dist_array)[1])
            k = k-1
    
        return result