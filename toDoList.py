class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False
    def  getTitle(self):
        return self.title
    def getDescription(self):
        return self.description
    def isCompleted(self):
        return self.completed
    def markCompleted(self):
        self.completed = True

class Node:
    def __init__(self, task):
        self.task = task
        self.next = None
class ToDoList:
    def __init__(self):
        self.head = None
    def addToDo(self,task):
        if self.head is None:
            self.head = Node(task)
        else:
            cur = self.head
            
            while cur.next is not None:
                cur = cur.next
            cur.next = Node(task)
    def markToDoAsCompleted(self,title):
        cur = self.head
        while cur is not None:
            if cur.task.getTitle() == title:
                cur.task.markCompleted()
                print('task marked as completed successfully')
                return
            cur = cur.next
        print('no such task')
    def viewToDoList(self):
        cur = self.head
        print('\n\n')
        while cur != None:
            print(f'task title: {cur.task.getTitle()}')
            print(f'task description: {cur.task.getDescription()}')
            print(f'is completed : {cur.task.isCompleted()}')
            
            print('|______________________|\n')
            cur = cur.next
main = ToDoList()
print('a --> to add task\nm--> to mark task as completed\nv --> to view to do list')
    
while True:
    
    cmd = input('enter your command: ')
    if cmd == 'a':
        title = input('enter the title of the task: ')
        des = input('enter description for the task: ')
        newTask = Task(title, des)
        main.addToDo(newTask)
        continue
    if cmd == 'm':
        title = input('Enter the title of task you want to mark as completed: ')
        main.markToDoAsCompleted(title)
        continue
    if cmd == 'v':
        main.viewToDoList()
        continue
    else:
        print('invalid input')
    