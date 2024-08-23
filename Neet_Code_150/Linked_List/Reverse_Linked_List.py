
## RECURSIVE METHOD: T:O(n), M:O(n)



## ITERATIVE METHOD: T:O(n), M:O(1)

## assign prev to None and head to current
## while curr is not None-> because after last node curr will be none
## assign curr.next node to temp variable next_node
# then set curr.next to prev
## then addisng prev to cutt
# assign curr to next_node

#return prev_node as curr is None



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # print(head)
        pre_node = None
        curr_node = head

        while curr_node:
            next_node = curr_node.next
            curr_node.next = pre_node

            pre_node = curr_node
            curr_node = next_node
       

        return pre_node