# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # so that self.res is accessible to also the dfs function
        self.res = 0

        def dfs(curr: TreeNode) -> int:
            if not curr:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)

            # post order, bcs we would like to get the result from bottom-up
            # this one is the one that saves/compare the width of the tree
            # hence we could just return res
            self.res = max(self.res, left + right)
            # this block actually only gives the current height of the subtree to above
            return 1 + max(left, right)
        
        # dont forget to call the recursive on the root!
        dfs(root)
        return self.res