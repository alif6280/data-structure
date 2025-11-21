class Stack:
    def __init__(self):
        self.x = []

    def push(self, value):
        self.x.append(value)

    def pop(self):
        if len(self.x) > 0:
            j=self.x.pop(0)
            print("Popped : ",j)
            print("after popped : ",self.x)
        else:
            print("Stack is empty")

    def top(self):
        if len(self.x) > 0:
            print("Top Element :", self.x[-1])
        else:
            print("Stack is empty")

    def empty(self):
        return len(self.x) == 0

    def size(self):
        return len(self.x)

    def insert(self, index, value):
        if index < 0 or index > len(self.x):
            print("Invalid Index")
            return
        self.x.insert(index, value)
        print("Inserted element : ",self.x)

    def deleteat(self, index):
        if index < 0 or index >= len(self.x):
            print("Invalid Index.")
            return
        self.x.pop(index)
        print("Delete element : ",self.x)

    def show(self):
        if len(self.x) == 0:
            print("Stack is empty")
            return
        print("Stack Elements:", *self.x)

s = Stack()

s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)

s.show()
s.top()
s.pop()
s.insert(1, 99)
s.deleteat(2)
s.show()
print("Empty ?", s.empty())
print("Size:", s.size())
