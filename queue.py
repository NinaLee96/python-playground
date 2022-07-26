
class Queue:
    def __init__(self):
        self.que = []
    
    def push(self, val):
        self.que.append(val)
    
    def pop(self, val):
        return print(self.que.pop(0))

    def get_size(self):
        return print(len(self.que))
    
    def print_q(self):
        if len(self.que) > 0:
            for element in self.que:
                print(element)
    
q = Queue()
q.push(5)
q.push(4)
q.push(2)
q.print_q()

  