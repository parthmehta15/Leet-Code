'''
 Floyd's Cycle Detection
 Cycle linked list problem (Find the starting of cycle)
 start with slow speed(1) and fast speed(2) pointers and find where they first meet]
 now start 2 new pointers from 0 and meeting point and with slow speed(1) and the new meeting point is the cycle start point

'''






class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        fast = fast
        slow = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                return fast
            