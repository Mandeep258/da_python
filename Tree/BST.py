class Node:
    def  __init__(self,data=None):
        self.data = data
        self.left_child = None
        self.right_child = None

    def insert(self,data):
        if self.data == data: #BST cannot have duplicate data
            return False
        elif data<self.data:
            if self.left_child:
                return self.left_child.insert(data)
            else:
                self.left_child = Node(data)
                return True
        else:
            if self.right_child:
                return self.right_child.insert(data)
            else:
                self.right_child = Node(data)
                return True

    def find_min(self,node):
        current = node
        while current.left_child is not None:
            current = current.left_child
        return current

    def find_max(self,node):
        current = node
        while current.right_child is not None:
            current = current.right_child
        return current

    def delete(self,data):
        if self is None:
            return None
        if data<self.data:
            self.left_child = self.left_child.delete(data)
        elif data>self.data:
            self.right_child = self.right_child.delete(data)
        else:
            if self.left_child is None:
                temp = self.right_child
                self = None
                return temp
            elif self.right_child is None:
                temp = self.left_child
                self = None
                return temp
            temp = self.find_min(self.right_child)
            self.data = temp.data
            self.right = self.right_child.delete(temp.data)
        return self

    def find(self,data):
        if data==self.data:
            return True
        elif data<self.data:
            if self.left_child:
                return self.left_child.find(data)
            else:
                return False
        else:
            if self.right_child:
                self.right_child.find(data)
            else:
                return False

    def preorder(self):
        if self:
            print(str(self.data), end=' ')
            if self.left_child:
                self.left_child.preorder()
            if self.right_child:
                self.right_child.preorder()

    def inorder(self):
        if self:
            if self.left_child:
                self.left_child.inorder()
            print(str(self.data), end=" ")
            if self.right_child:
                self.right_child.inorder()

    def postorder(self):
        if self:
            if self.left_child:
                self.left_child.postorder()
            if self.right_child:
                self.right_child.postorder()
            print(str(self.data), end=' ')

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def delete(self,data):
        if self.root is not None:
            self.root.delete(data)

    def find(self,data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        if self.root is not None:
            print()
            print('preorder:')
            self.root.preorder()

    def inorder(self):
        if self.root is not None:
            print()
            print('inorder:')
            self.root.inorder()

    def postorder(self):
        if self.root is not None:
            print()
            print('postorder:')
            self.root.postorder()
