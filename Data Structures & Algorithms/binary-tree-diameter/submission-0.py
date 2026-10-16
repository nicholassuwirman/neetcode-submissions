# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # so that self.diameter is accessible to also the dfs function
        self.diameter = 0

        def dfs(curr: TreeNode) -> int:
            if not curr:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)

            # post order, bcs we would like to get the result from bottom-up
            self.diameter = max(self.diameter, left + right)
            return 1 + max(left, right)
        
        # dont forget to call the recursive on the root!
        dfs(root)
        return self.diameter