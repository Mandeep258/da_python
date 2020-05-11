class ET:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def isOperator(c):
    if (c=='+' or c=='-' or c=='*' or c=='/' or c=='^'):
        return True
    return False

def inorder(t):
    if t is not None:
        inorder(self.left)
        print(t.value)
        inorder(self.right)

def constructionTree(postfix):
    stack = []
    for char in postfix:
        if not isOperator(char):
            t = ET(char)
            stack.append(t)
        else:
            t = ET(char)
            t1 = stack.pop()
            t2 = stack.pop()
            t.right = t1
            t.left = t2
            stack.append(t)
    t=stack.pop()
    return t

postfix = "ab+fe*g*-"
r = constructionTree(postfix)
inorder(r)
