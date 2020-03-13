class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        if temp == None:
            print("List is empty?")
        while(temp):
            print(temp.data,end = " ")
            temp = temp.next
        print("\n")

    def insertlst(self,new_data):
        new_node = Node(new_data)
        temp = self.head
        if temp.next == None:
            temp.next = new_node
            return
        while(temp.next != None):
            temp = temp.next
        temp.next = new_node

    def deleteList(self):
        self.head = None

    def middleNode(self):
        temp = self.head
        tempp = temp.next
        while(tempp):
            temp = temp.next
            tempp = tempp.next
            tempp = tempp.next
        print("Middle Element is:: ",temp.data)

if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second
    second.next = third

    llist.printList()
    llist.insertlst(34)
    llist.insertlst(4)
    llist.insertlst(64)
    llist.insertlst(61)
    llist.printList()
    # llist.deleteList()
    # llist.printList()
    llist.middleNode()


