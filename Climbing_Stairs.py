class Solution:
    def climbStairs(self, n: int) -> int:

####################################################################
        # RECURSION
        # def find_ways(n):
        #     if n == 2:
        #         return 2
        #     elif n == 1:
        #         return 1
        #     else:
        #         return find_ways(n-1) + find_ways(n-2)
        #     # return n

        # return find_ways(n)
        
####################################################################
        # BOTTOM UP ( In how many was u can rreach top from a point )
        if n == 1:
            return 1
        if n == 2:
            return 2

        s1 = 1
        s2 = 1
        for i in range(n-2):
            temp = s1+s2
            s1 = s2
            s2 = temp
        return(s2+s1)


            