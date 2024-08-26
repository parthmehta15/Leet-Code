'''
Use heap to keep track

'''

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        for i in range(len(stones)):
            stones[i] = -1*stones[i]
        heapq.heapify(stones)
        while len(stones)>2:
            a = heapq.heappop(stones)
            b = heapq.heappop(stones)

            if a == b:
                continue
            if -1*a > -1*b:
                heapq.heappush(stones, -1*(-1*a-(-1*b)))

        if len(stones) == 1:
            return -1 * stones[0]
        elif stones[0] == stones[1]:
            return 0 
        else:
            return -1* stones[0] - (-1* stones[1])

        