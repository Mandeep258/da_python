class Node:

    def __init__(self, data = None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class SinglyLinkedList:

    def __init__(self):
        self.tail = None
        self.head = None

    def append_long(self, data):
        node = Node(data)
        if self.tail == None:
            self.tail = Node
        else:
            current = self.tail
            while current.next:
                current = current.next
            current.next = node

    def append(self, data):
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node
