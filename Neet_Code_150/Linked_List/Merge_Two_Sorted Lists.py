

#LIST NODE -> ITS NOT A LIST BUT A LIST NODE
# Start with assigning a empty new_node 
# Then while true 
# if l1<l2 add to new_node -> update l1, and tail
# else add l2 to new_node -> update l2, and tail
# Also check if any list empty, then add entire list to tail
# Return new_node.next as the first elemnt is dummy



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        newList = ListNode()
        tail = newList

        while True:
            if list1 == None:
                tail.next = list2
                break
            if list2 == None:
                tail.next = list1
                break

            if list1.val<=list2.val:
                tail.next = list1
                list1 = list1.next
                tail = tail.next
            else:
                tail.next = list2
                list2 = list2.next
                tail = tail.next
                
        
        return newList.next