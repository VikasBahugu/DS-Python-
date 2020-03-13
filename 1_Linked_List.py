class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data,end=" ")
            temp = temp.next
        print("\n")

    #Add element in the frount of list.
    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    #Add at particular element
    def insert_after(self,prev_node,new_data):
        if prev_node is None:
            print("Element does'nt exist.")
            return
        new_node = Node(new_data)
        temp = self.head
        while(temp.data != prev_node):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    #Add at last of LL
    def insert_last(self,new_data):
        new_node = Node(new_data)
        temp = self.head
        if temp.next == None:
            print("Linked list is empty")
        else:
            while(temp.next != None):
                temp = temp.next
        temp.next = new_node



if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(4)
    third = Node(3)
    llist.head.next = second
    second.next = third

    print("Inseted Elements are:")
    llist.printList()
    print("Element is being pushed at the starting of LL:")
    llist.push(34)
    llist.printList()
    print("Element is being pushed after specific node:")
    llist.insert_after(1,33)
    llist.printList()
    print("Element is being pushed at the end of LL:")
    llist.insert_last(56)
    llist.printList()