# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:    # if both nodes are Null
            return True


        if p and not q:        # if node p exists and node q Null
            return False
        if not p and q:        # if node p Null and node q exists
            return False

        if p.val != q.val:     # if value is different we can simply return false
            return False
        if p.val == q.val:     # on the case you want to traverse, dont return! call the function recursively
            return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
            
            


        
        