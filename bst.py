#BST
class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def insert(root, data):
    if root is None:
        return Node(data)

    else:
        if data > root.data:
            root.right = insert(root.right, data)
        if data < root.data:
            root.left = insert(root.left, data)
    
    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

def get_size(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1
    
    else:
        return 1+ get_size(root.left) +get_size(root.right)

def inorder_it(root):
    stack = []
    current = root
    while current is not None:
        stack.append(current)
        #print(current.data, 'appended')
        current = current.left
    
    #print_stack()
    while len(stack)!= 0 and current is None:
        elem = stack.pop()
        print(elem.data)
        current = elem.right

        while current is not None:
            stack.append(current)
            current = current.left

def preorder_it(root):
    stack = []
    current = root
    print(current.data)
    if current.right is not None:
        stack.append(current.right)
    if current.left is not None:
        stack.append(current.left)
    while len(stack) != 0:
        current = stack.pop()
        print(current.data)
        if current.right is not None:
            stack.append(current.right)
        if current.left is not None:
            stack.append(current.left)
    

def postorder_it(root):
    stack_1 = []
    stack_2 = []
    current = root
    stack_1.append(current)
    while len(stack_1)!=0:
        elem = stack_1.pop()
        stack_2.append(elem)
        if elem.left is not None:
            stack_1.append(elem.left)
        if elem.right is not None:
            stack_1.append(elem.right)

    while len(stack_2)!=0:
        print(stack_2.pop().data)


def levelorder(root):
    if root is None:
        return
    queue = []
    queue.append(root)
    while len(queue)!=0:
        elem = queue.pop(0)
        print(elem.data)
        if elem.left is not None:
            queue.append(elem.left)
        if elem.right is not None:
            queue.append(elem.right)
        


n = Node(10)
insert(n, 5)
insert(n, 15)
insert(n, 7)
insert(n, 1)
insert(n, 17)
insert(n, 19)
#insert(n, 4)

#8 1 5 N 7 10 6 N 10 6

#9 3 10 9 N 7 4 7

#inorder_it(n)
#preorder_it(n)
#postorder_it(n)
levelorder(n)