from Create_linked_list import Node, LinkedList


#List 1
Node1 = Node(1)
Node2 = Node(3)
Node3 = Node(4)

firstList = LinkedList()
firstList.insertEnd(Node1)
firstList.insertEnd(Node2)
firstList.insertEnd(Node3)


#List 2
Node4 = Node(2)
Node5 = Node(7)
Node6 = Node(9)

secondList = LinkedList()
secondList.insertEnd(Node4)
secondList.insertEnd(Node5)
secondList.insertEnd(Node6)

print('First list')
firstList.print_list()
print('Second list')
secondList.print_list()



def merge_lists(firstList, secondList):
    mergedList = LinkedList()


    currFirst = firstList.head
    currSecond = secondList.head

    while True:
        
        if currFirst is None:
            mergedList.insertEnd(currSecond)
            break

        if currSecond is None:
            mergedList.insertEnd(currFirst)
            break
        

        if currFirst.data < currSecond.data:
            dummy = currFirst.next
            currFirst.next = None
            mergedList.insertEnd(currFirst)
            currFirst = dummy

            

        else:
            dummy = currSecond.next
            currSecond.next = None
            mergedList.insertEnd(currSecond)
            currSecond = dummy


    return mergedList


megrgedList = merge_lists(firstList, secondList)
print('Merged List')
megrgedList.print_list()