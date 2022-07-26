
# Stack

# - LIFO
# - FIFO
# - Push and pop are O(1) time complexity
# 


class Stack:
    def __init__(self) -> None:
        self.stack = []
    
    def pop(self):
        if len(self.stack) != 0:
             self.stack.pop()

    def __len__(self):
        return len(self.stack)

    def push(self, val):
        self.stack.append(val)
    
    def getLength(self):
        m = len(self.stack)
        return print(m)
    
    def viewStack(self):
        if len(self.stack) > 0:
            for i in self.stack:
                print(i)
    


s = Stack()
s.push(1)
s.push(2)
s.push(3)
# s.viewStack()
s.getLength()

