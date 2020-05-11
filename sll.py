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
        self.size = 0

    def append_long(self, data):
        node = Node(data)
        if self.tail == None:
            self.tail = Node
        else:
            current = self.tail
            while current.next:
                current = current.next
            current.next = node
        self.size+=1

    def append(self, data):
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node
        self.size+=1

    def push(self, data):
        node = Node(data):
        if self.tail is None:
            self.tail = node
            self.head = node
            return
        node = self.tail
        self.tail=node

    def size(self):
        count = 0
        current = self.tail
        while current:
            count+=1
            current = current.next
        return count

    def iter(self):
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val

    def delete(self, data):
        current = self.tail
        prev = self.tail
        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    prev.next = current.next
                self.size-=1
                return
            prev = current
            current = current.next

    def search(self,data):
        for i,node in enumerate(self.iter()):
            if data == node:
                return "{0} is present at position {1}".format(data,i)
            return "{data} is not present".format(data = data)

    def clear(self):
        self.tail = None
        self.head = None


    def reverse(self):
        prev = None
        current = self.tail
        while current:
            next_ = current.next
            current.next = prev
            prev = current
            current = next_
        self.tail = prev

    def reverse_util(self, curr, prev):
        if curr.next is None:
            self.head = curr
            curr.next = prev
            return
        next_ = curr.next
        curr.next = prev
        self.reverse_util(next,curr)

    def reverse_recursive(self):
        if self.tail is None:
            return
        self.reverse_util(self.tail,None)
