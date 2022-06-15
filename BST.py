class Node():
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root is None:
            self.root = Node(data)

        else:
            self._insert(data,self.root)

    def _insert(self,data,curr):
        if data<curr.val:
            if curr.left is None:
                curr.left = Node(data)
            else:
                self._insert(data,curr.left)
        elif data>curr.val:
            if curr.right is None:
                curr.right = Node(data)
            else:
                self._insert(data,curr.right)
        else:
            return

    def find(self,data):
        if self.root:
            return self._find(data,self.root)
        else:
            None
    
    def _find(self,data,curr):
        if curr is None:
            return False

        if data == curr.val:
            return True
        elif data<curr.val:
            return self._find(data,curr.left)
        else:
            return self._find(data,curr.right)



bst = BST()
bst.insert(10)
bst.insert(5)
bst.insert(12)
bst.insert(3)
bst.insert(8)
print(bst.find(10))
