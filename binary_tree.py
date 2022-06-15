from collections import deque

class Stack():
    def __init__(self):
        self.items = deque()

    def push(self,val):
        self.items.append(val)

    def pop(self):
        return self.items.pop()
    
    def isEmpty(self):
        return len(self.items) == 0

class Queue():
    def __init__(self):
        self.items = deque()

    def enqueue(self,val):
        self.items.append(val)

    def dequeue(self):
        if len(self.items):
         return self.items.popleft()

    def isEmpty(self):
        return len(self.items) == 0
    


class Node():
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class binaryTree():
    def __init__(self,root):
        self.root = Node(root)

    def preorder(self,st,trav):

        if st:
            trav += (str(st.val) + "-")
            trav = self.preorder(st.left,trav)
            trav = self.preorder(st.right,trav)
        return trav

    def iterPreorder(self,st):
        s = Stack()
        s.push(st)
        r = ""

        while not s.isEmpty():
            p = s.pop()
            r += str(p.val) + "-"

            if p.right:
                s.push(p.right)
            if p.left:
                s.push(p.left)

        return r
    
    def postorder(self,st,trav):
        if st:
            trav = self.postorder(st.left,trav)
            trav = self.postorder(st.right,trav)
            trav += (str(st.val) + "-")
        return trav

    def iterPostorder(self,st):
        s1 = Stack()
        s1.push(st)
        s2 = Stack()

        while not s1.isEmpty():
            p = s1.pop()
            s2.push(p.val)
            if p.left:
                s1.push(p.left)
            if p.right:
                s1.push(p.right)

        r = ''
        while not s2.isEmpty():
            r += str(s2.pop()) + "-"
        return r





    def inorder(self,st,trav):
        if st:
            trav = self.inorder(st.left,trav)
            trav += (str(st.val) + "-")
            trav = self.inorder(st.right,trav)
        return trav

    def iterativeInorder(self,st):
        curr = st
        r = ''
        s = Stack()
        while True:
            if curr is not None:
                s.push(curr)
                curr = curr.left

            elif not s.isEmpty():
                p = s.pop()
                r += str(p.val) + "-"
                curr = p.right

            else:
                break
        
        return r


    def rlevelorder(self,st):
        if st is None:
            return 

        q = Queue()
        s = Stack()

        q.enqueue(st)

        while not q.isEmpty():
            node = q.dequeue()
            s.push(node.val)

            if node.right:
                q.enqueue(node.right)
            if node.left:
                q.enqueue(node.left)

        trav = ""
        while not s.isEmpty():
            trav += str(s.pop()) + "-"

        return trav


    def levelorder(self,st):
        if st is None:
            return
        q = Queue()
        q.enqueue(st)
        trav = ""

        while not q.isEmpty():
            node = q.dequeue()
            trav += str(node.val) + "-"

            if node.left:
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right)

        return trav

    def height(self,st):
        if st is None:
            return -1

        lh = self.height(st.left)
        rh = self.height(st.right)

        return 1+max(lh,rh)


tree = binaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7) 
print(tree.preorder(tree.root,""))
print(tree.postorder(tree.root,""))
print(tree.inorder(tree.root,""))
print(tree.levelorder(tree.root))
print(tree.rlevelorder(tree.root))
print(tree.height(tree.root))
print(tree.iterativeInorder(tree.root))
print(tree.iterPreorder(tree.root))
print(tree.iterPostorder(tree.root))