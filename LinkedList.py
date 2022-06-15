class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new = Node(data)

        if self.head is None:
            self.head = new
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new

    def prepand(self,data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def print(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next
          
    def insertAfterNode(self,n,data):
        new = Node(data)
        curr = self.head
        while curr.data!=n:
            curr = curr.next
        
        new.next = curr.next
        curr.next = new

    def delete(self,key):
        curr = self.head

        if curr and curr.data == key:
            self.head = curr.next
            curr.next = None
            return
        pre = None
        while curr and curr.data!=key:
            pre = curr
            curr = curr.next

        if curr is None:
            return
        pre.next = curr.next
        curr.next = None

    def length(self):
        curr = self.head
        l = 0
        while curr:
            l+=1
            curr = curr.next
        print(l)

myList = LinkedList()
myList.append("A")
myList.append("B")
myList.append("C")
myList.append("D")        
myList.insertAfterNode("B","E")
myList.delete("X")
myList.print()
myList.length()