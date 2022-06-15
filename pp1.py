class Node:
    def __init__(self,val):
        self.val = val 
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self,data,currNode):
        if self.root is None:
            self.root = Node(data)

        elif data > currNode.val:
            if currNode.right is None:
                currNode.right = Node(data)
            else:
                self.insert(data,currNode.right)
        elif data < currNode.val:
            if currNode.left is None:
                currNode.left = Node(data)
            else:
                self.insert(data,currNode.left)
        else:
            print("Value is already present in tree")

    def preOrder(self,st,trav):
        if st:
            trav += str(st.val)+"-"
            trav = self.preOrder(st.left,trav)
            trav = self.preOrder(st.right,trav)
        return trav

    def find(self,data):
        if self.root:
            is_found = self._find(data,self.root)
            if is_found:
                return True
            return False
        else:
            return None

    def _find(self,data,currNode):
        if data < currNode.val and currNode.left:
            return self._find(data,currNode.left)
        
        elif data > currNode.val and currNode.right:
            return self._find(data,currNode.right)

        elif data == currNode.val:
            return True


tree = BST()
tree.insert(8,tree.root)
tree.insert(3,tree.root)
tree.insert(10,tree.root)
tree.insert(1,tree.root)
tree.insert(6,tree.root)
tree.insert(7,tree.root)
tree.insert(12,tree.root)
print(tree.preOrder(tree.root,''))
print(tree.find(12))