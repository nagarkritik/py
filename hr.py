from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestUnivaluePath(self, root):
        h = 0
        q = deque([(root,0)])

        while q:
            a = q.popleft()

            if a[1] > h:
                h = a[1]

            if a[0].left and a[0].right:
                if a[0].left.val == a[0].val:
                    q.append((a[0].left,a[1]+1))
                else:
                    q.append((a[0].left,0))
            if a[0].right:
                if a[0].right.val == a[0].val:
                    q.append((a[0].right,a[1]+1))
                else:
                    q.append((a[0].right,0))

        return h


root = TreeNode(2)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(5)
root.left.right = TreeNode(7)
#root.right.right = TreeNode(7)
#root.left.left.left = TreeNode(1)

s = Solution()
print(s.longestUnivaluePath(root))

