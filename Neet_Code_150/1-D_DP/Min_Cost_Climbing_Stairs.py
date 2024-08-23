'''
Similar to Climbing Staris
Last term as one, second last as two

Then loop in reverse range(n-2)
Update two with min(cost[i]+one, cost[i]+two)
one with two byt first keeping two in dummy

since you can start from index 0 or 1 
return min (one, two)




'''




class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one = cost[-1]
        two = cost[-2]
        n = len(cost)
        for i in reversed(range(n-2)):
            dummy = two
            two = min(cost[i]+one, cost[i]+two)
            one = dummy
        
        return min(one, two)
        