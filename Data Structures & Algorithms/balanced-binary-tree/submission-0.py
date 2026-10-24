# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# postorder DFS, check no 2 at notes

class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        # flag
        self.balanced = True

        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            if abs(left - right) > 1:
                self.balanced = False
            
            return 1 + max(left, right)

        dfs(root)
        
        if self.balanced:
            return True
        else:
            return False