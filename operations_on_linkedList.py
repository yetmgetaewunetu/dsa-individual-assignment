class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

class Operations_on_LinkedList:
    def __init__(self):
        self.head = None
    def insertAtPos(self, pos, val):
        if self.head is None:#if the head is none i want to make the new value a head
            self.head = Node(val)
            
            return
        #if self.head is not none i will traverse the linkedlist until i reach pos - 1, i used pos - 1 to find the previous node before that position
        cur = self.head
        position_counter = 0
        while cur != None:
            if position_counter == pos - 1:
                newNode = Node(val)
                
                newNode.next = cur.next
                cur.next = newNode
                return
            cur = cur.next
            position_counter += 1
        #if there is no return inside the loop that means the given index is greater the number of elements available
        print(f"position {pos} is out of bound")
    def deleteAtPosition(self, pos):
        if pos == 1:#this means the head is the one to be deleted
            self.head = self.head.next
            return
        if pos <= 0:
            print('minimum index is 1')
            return
        cur = self.head
        pos_cnt = 1
        while cur.next != None:
            if pos_cnt == pos -1:
                cur.next = cur.next.next
                return
            cur = cur.next
        #if there is no return inside the loop that means the given index is greater the number of elements available
        print(f"index {pos} is out of bound")
    def deleteAfterNode(self, data):
        cur = self.head
        while cur!= None:
            if cur.val == data:
                
                cur.next = cur.next.next if cur.next is not None else None
                return
            cur = cur.next
        #the indicated data is not in the linked list
        print("the items is not in the list")
    def searchNode(self, data):
        cur = self.head
        while cur is not None:#traversing the whole linked list first
            if cur.val == data:
                print("item is found")
                return
            cur = cur.next
        print('item is not in the list')
    def view(self):
        cur = self.head
        while cur is not None:
            print(cur.val)
            cur = cur.next

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
    def push(self, data):
        if self.head is None:
            self.head = Node(data)
            self.size = 1
            return
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)
        self.size += 1
        
    def pop(self):
        if self.head is None:
            return -1
        if self.head.next is None:
            self.size -= 1
            temp = self.head
            self.head = None
            return temp
        cur = self.head
        while cur.next.next is not None:
            cur = cur.next
        cur.next = None
        self.size -= 1
    def peek(self):
        cur = self.head
        if self.head is None:
            return -1
        while cur.next != None:
            cur = cur.next
        return cur.val
    def getSize(self):
        return self.size
    
    def printStack(self):
        cur = self.head
        while cur != None:
            print(cur.val)
            cur = cur.next

main = Operations_on_LinkedList()

    
main.insertAtPos(0, 1)
main.insertAtPos(1, 2)
main.insertAtPos(2, 3)
main.insertAtPos(1, 4)
#main.insertAtPos(8, 1)
#main.searchNode(3)
#main.view()
main.deleteAtPosition(1)
#main.view()
#main.deleteAtPosition(5)
main.deleteAfterNode(2)
#main.searchNode(3)
#main.view()
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
#stack.pop()
#print(stack.peek())
stack.printStack()
print(stack.getSize())