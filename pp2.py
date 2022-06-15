# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root):
        
        if root is None:
            return root
        
        l1 = [root]
        r = [[root.val]]
        
        while len(l1):
            l2 = []
            t = []
            while len(l1):
                e = l1.pop(0)
                if e.left:
                    l2.append(e.left)
                    t.append(e.left.val)
                if e.right:
                    l2.append(e.right)
                    t.append(e.right.val)
            
            if len(t):
                r.append(t)
            l1+=l2
        
        return r

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

s = Solution()
print(s.levelOrder(root))
