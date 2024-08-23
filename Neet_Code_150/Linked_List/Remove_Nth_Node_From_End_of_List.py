
'''
Other solution using 2 pointers 
Assigning dummy variable and having left at that point and right shifter by n from first element,
Benefit is that edge cases are taken care of

'''




'''
Faster using 2 pointers
if head.next is None that is only one element than return None
left pointer at head, right is shifter by n times
when right reaches en, left element needs to be deleted, keep track of prev_left and then link it to next left
Also keep track of count, if count is zero that is right already at None :
means that n == len(list) and therefore return head.next


'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head.next == None:
            head = None
            return

        left = head
        right = head
        for i in range(n):
            right = right.next
        prev_left = None
        count = 0
        while right:
            prev_left = left
            left = left.next
            right = right.next
            count += 1
    
        if count == 0:
            return head.next


        prev_left.next = left.next
        left.next = None
        return head


'''
Slow solution:
1. Edge case: if head.next is None that is only one element than return None

2. Find length of list, if lenght == n then remove first element and return 

3. Find n position form start of list and than remove
'''



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            head = None
            return

        count = 0
        curr_node = head
        while curr_node:
            count = count + 1
            curr_node = curr_node.next
        if count == n:
            return head.next
        curr_node = head
        for i in range(count - n):
            prev_node = curr_node
            curr_node = curr_node.next
        
        prev_node.next = curr_node.next
        curr_node.next = None

        return head
        