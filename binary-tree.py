import collections
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def printInOrder(root):
    if root:
        printInOrder(root.left)
        print(root.val)
        printInOrder(root.right)

def printPostOrder(root):
    if root:
        printInOrder(root.left)
        printInOrder(root.right)
        print(root.val)

def printPreorder(root):
    if root:
        print(root.val)
        printInOrder(root.left)
        printInOrder(root.right)

# invert binary tree 
def bfs(root):
    queue = collections.deque([(root)])

    while queue:
        node = queue.popleft()
        if node:
            node.left, node.right = node.right, node.left
            queue.append(node.left)
            queue.append(node.right)
    return root

# invert binary tree, dfs
def dfs(root):
    stack = [root]

    while stack:
        node = stack.pop()
        if node:
            node.left, node.right = node.left, node.right
            stack.append(node.left)
            stack.append(node.right)
    return root

# gets max depth of a binary tree with dfs
def dfs_get_max_depth(root):
    stack = [(1, root)]
    maxDepth = 0
    while stack:
        depth, node = stack.pop()
        if node:
            maxDepth = max(maxDepth, depth)
            stack.append((depth+1, node.left))
            stack.append((depth+1, node.right))
    return print(maxDepth)

# ==================================================================================

# main driver
def tree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    # print ("Preorder traversal of binary tree is")
    # printPreorder(root)
    # print ("\nInorder traversal of binary tree is")
    # printPostOrder(root)
    # print ("\nPostorder traversal of binary tree is")
    # printInOrder(root)

    # tree = bfs(root)
    # dfstree = dfs(root)
    # printInOrder(dfstree)

    # dfs_get_max_depth(root)


tree()
# ==================================================================================
# ==================================================================================
# stack implementation
def inOrder(root):
    current = root
    stack = [] 
    while True:
        if current is not None:
            stack.append(current)
            current = current.left
        elif(stack):
            current = stack.pop()
            print(current.val)
            current.right
        else:
            break
    print()
    
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
 
# inOrder(root)


