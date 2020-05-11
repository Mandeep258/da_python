from collections import deque
class Node:
    def __init__(self,data):
        self.data = data
        self.right_child = None
        self.left_child = None

    def dfs_inOrder(self, root_node):
        current = root_node
        if current is None:
            return
        self.dfs_inOrder(current.left_child)
        print(current.data)
        self.dfs_inOrder(current.right_child)


    def dfs_preOrder(self, root_node):
        current = root_node
        if current is None:
            return
        print(current.data)
        self.dfs_preOrder(current.left_child)
        self.dfs_preOrder(current.right_child)

    def dfs_postOrder(self, root_node):#reverse polish notation
        if root_node is None:
            return
        self.dfs_postOrder(root_node.left_child)
        self.dfs_postOrder(root_node.right_child)
        print(root_node.data)

    def height(self,root_node):
        if root_node is None:
            return 0
        else:
            lheight = self.height(root_node.left_child)
            rheight = self.height(root_node.right_child)

            if lheight>rheight :
                return  lheight+1
            else:
                return rheight+1

    def bfs(self,root_node):
        q=[]
        traversal_queue = deque([root_node])
        while len(traversal_queue) > 0:
            node = traversal_queue.popleft()
            q.append(node.data)
            if q.left_child:
                traversal_queue.append(node.left_child)
            if q.right_child:
                traversal_queue.append(node.right_child)
            return q
