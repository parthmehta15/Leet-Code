

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def isListEmpty(self):
        if self.head is None:
            return True
        else:
            return False
        
    def listLength(self):
        count = 0
        currNode = self.head
        while currNode is not None:
            count = count+1
            currNode = currNode.next
        return count
        

    def insert(self, newNode):
        if self.head == None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                else:
                    lastNode = lastNode.next 

            lastNode.next = newNode

    def insertHead(self, newNode):
        if self.head == None:
            self.head = newNode
        else:
            dummy = self.head
            self.head = newNode
            self.head.next = dummy
            del dummy

    def insertAt(self, newNode, pos):
        if pos< 0 or pos > self.listLength():
            print('Invalid position')
            return -1

        if pos == 0:
            self.insertHead(newNode)
            return

        currNode = self.head
        curr_pos = 0
        while True:
            if curr_pos == pos:
                prevNode.next = newNode
                newNode.next = currNode
                break 
            prevNode = currNode
            currNode = currNode.next
            curr_pos += 1


    def insertEnd(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode


    def deleteHead(self):
        if self.isListEmpty() is False:
            dummy = self.head
            self.head = self.head.next
            dummy.next = None
        else:
            print('List empty')

    def deleteAt(self, pos):

        if pos < 0 or pos >= self.listLength():
            print('invalid pos')
            return

        if self.isListEmpty() is False:
            if pos == 0:
                self.deleteHead()
                return
            idx = 0
            currNode = self.head
            while True:
                if idx == pos:
                    prevNode.next = currNode.next
                    currNode.next = None
                    break
                prevNode = currNode
                currNode = currNode.next
                idx += 1

        else:
            print('List is Empty')

    
    def deleteEnd(self):
        lastNode = self.head
        while lastNode.next is not None:
            prevNode = lastNode
            lastNode = lastNode.next

        prevNode.next = None
        del lastNode

        
    def print_list(self):
        if self.head is None:
            print("List Empty")
            return
        currNode = self.head

        while True:
            if currNode is None:
                break 
            print(currNode.data)
            currNode = currNode.next
            


if __name__ == "__main__":
    linked_list = LinkedList()

    first_node = Node(10)
    linked_list.insert(first_node)

    second_node = Node(20)
    linked_list.insert(second_node)

    third_node = Node(15)
    linked_list.insertAt(third_node, 1)

    linked_list.deleteAt(3)

    linked_list.print_list()