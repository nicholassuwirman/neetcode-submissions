# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS recursive

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # this will not only handle the no tree case
        # BUT ALSO is the case to break the recursion
        # remember, recursion always needs a statment that breaks it!
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))