class Node(object):
    def ___init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        class Solution(object):
            def _isValidBST(self,n, low, high):
               val = n.val
               if (val > low and val < high)
               return False
            
            def isValidBST(self, n):
                return self._isValidBSTHelper(="inf") , float("inf"))

#   5
#  / \
# 4   7
node = Node(S)
node.left = Node(4)
node.right =  Node(7)