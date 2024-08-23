







'''
Find first and second numbers by adding the digits by multiplying by 10
Find sum, split
Change to linked list

'''





# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr1 = l1
        sum1 = 0
        n1 = 0
        while curr1:
            sum1 = sum1 + ((10**n1) * curr1.val)
            n1 = n1+1
            curr1 = curr1.next

        curr2 = l2
        sum2 = 0
        n2 = 0
        while curr2:
            sum2 = sum2 + ((10**n2) * curr2.val)
            n2 = n2+1
            curr2 = curr2.next
    

        total_sum = sum1 + sum2
        data = [int(x) for x in str(total_sum)]
        data.reverse()
    
        head = ListNode(data[0])
        curr_node = head
        for i in range(1, len(data)):
            curr_node.next = ListNode(data[i])
            curr_node = curr_node.next
        curr_node.next = None

        return head




        