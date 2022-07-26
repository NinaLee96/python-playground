class Node:
  def __init__(self, val=None, nxt=None):
    self.val = val
    self.next = nxt

class LinkedList:
  def __init__(self) -> None:
      self.head = None
  
  def insert(self, val):
      newNode = Node(val)
      if self.head:
        curr = self.head
        while curr and curr.next:
          curr = curr.next
        curr.next = newNode
      else:
        self.head = newNode

  def printList(self):
    while self.head:
      print(self.head.val)
      self.head = self.head.next

list1 = LinkedList()
list1.insert(0)
list1.insert(3)
list1.insert(4)
list1.insert(5)
list1.printList()

  

