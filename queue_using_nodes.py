class Node(object):
    def __init__(self, data=None, next=None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            node.prev=self.tail
            self.tail.next = node
            self.tail = node
        self.size+=1

    def dequeue(self):
        current = self.head
        if self.size == 1:
            self.head = None
            self.tail = None
        elif self.size>1:
            self.head = self.head.next
            self.head.prev = None
        self.size-=1
