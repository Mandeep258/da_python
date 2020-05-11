class Node(object):
    def __init__(Self,data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList(object):
    def __init__(self):
        self.head = None#beginner node
        self.tail = None #latest node
        self.count = 0

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.count+=1

    def delete(self, data):
        current = self.head
        node_deleted = False
        if current is None:
            node_deleted = False
            print("List is empty.")
        elif current.data == data:
            self.head = current.next
            self.head.prev = None
            node_deleted = True
        elif self.tail == data:
            self.tail = self.tail.prev
            self.tail.next = None
            node_deleted = True
        else:
            current=current.next
            while current:
                if current.data == data:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    node_deleted = True
                current = current.next

        if node_deleted:
            self.count-=1

    def contain(self,data):
        for node_data in self.iter():
            if data == node_data:
                return True
        return False

    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val
