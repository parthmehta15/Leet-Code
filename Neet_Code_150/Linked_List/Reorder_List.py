
# Split list into 2 and then add them alternately
# To split in 2 find middle element for that have 2 pointers 
# 1 slow start and other fast at start.next
# When fast reaches None stop and slow.next is the start of second list

#Then reverse the second list

# Then merge


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #Find middle
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
            fast = fast.next
        
        #Reverse second
        second = slow.next
        slow.next = None
        prev_node = None
        while second:
            next_node = second.next
            second.next = prev_node
            prev_node = second
            second = next_node

        #Merge
        start = head
        end = prev_node

        while True:
            if end == None:
                break
            new_start = start.next
            new_end = end.next
            start.next = end
            end.next = new_start
            start = new_start
            end = new_end
            
