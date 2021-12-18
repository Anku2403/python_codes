class Node:

#Creating new node
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linkedList:

    def __init__(self):
        self.head = Node()

#Inserting node from the end.
    def insertNode(self, data):
        newNode = Node(data)
        current = self.head
        if current is None:
            self.head = newNode
            return
        else:
            while(current.next):
                current = current.next
            current.next = newNode

#Deleting node from the end
    def deleteNode(self):
        current = self.head
        if current is None:
            print ("Linked List is empty")
            return
        else:
            while(current.next.next):
                current = current.next
            current.next = None 

#Inserting node at given index
    def insertNodeAt(self, index, data):
        if index<0 or index>=self.sizeLL():
            raise Exception("Invalid index")
        
        if index == 0:
            node = Node(data)
            node.next = self.head
            self.head = node

        count = 0
        current = self.head
        while current:
            if count == index-1:
                node = Node(data)
                node.next = current.next
                current.next = node
                break

            current = current.next
            count += 1

#Deleting node for any given index
    def deleteNodeAt(self, index):
        if index<0 or index>=self.sizeLL():
            raise Exception("Invalid index")

        if index==0:
            self.head = self.head.next
            return
        
        count = 0
        current = self.head
        while current:
            if count == index - 1:
                current.next = current.next.next
                break
            current = current.next
            count += 1

#Size of Linked list
    def sizeLL(self):
        count = 0
        current = self.head
        while(current.next):
            count += 1
            current = current.next
        print("Size of linked list is {}".format(count))
        return count

#Display linked list
    def displayLL(self):
        ele = []
        current = self.head
        while(current.next):
            current = current.next
            ele.append(current.data)
        print(ele)

my_List = linkedList()
my_List.displayLL()
my_List.insertNode(19)
my_List.insertNode(28)
my_List.insertNode(20)
my_List.displayLL()
my_List.insertNodeAt(0,10)
my_List.displayLL()
my_List.sizeLL()
#my_List.deleteNodeAt(2)
#my_List.displayLL()