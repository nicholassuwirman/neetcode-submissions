# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# First hint:
# the only possible way that marks a possible subroot existing in a root tree, is when the value is the same
# if we compare 1 == 2, it's obviously not the same, hence it's cant be a possible same subtree there

# preorder DFS

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        # same value marks a potential same subtree, hence call isSameTree next up to check
        # if both true and true, it means that the subtree exist, hence return true
        if root.val == subRoot.val and self.isSameTree(root, subRoot):
            return True

        # if above case is false, recursively call isSubTree to check further
        # use or here as the subtree can exist on the left or the right version
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p and q:
            return False
        if p and not q:
            return False

        if p.val != q.val:
            return False
        else:
            return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))