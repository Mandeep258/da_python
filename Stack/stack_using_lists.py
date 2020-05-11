class Stack:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return self.items==[]

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

if __name__="__main__":
    s=Stak()
    print(s.is_empty())
    s.push(4)
    s.push(5)
    s.push(3)
    s.peek()
    print(s.pop())
    print(s.size())
