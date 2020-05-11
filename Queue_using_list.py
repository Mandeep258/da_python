class Queue:

    def __init__(self):
        self.items = []
        self.size = 0
    def is_empty():
        return self.items == []

    def enqueue(self,item):
        self.size+=1
        self.items.insert(0,item)

    def dequeue(self):
        data = self.items.pop()
        self.size-=1
        return data

    def size(self):
        return len(self.items)


if __name__="__main__":
    q= Queue()
    q.enqueue(1)
    print(q.is_empty())
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())
    print(q.size)
